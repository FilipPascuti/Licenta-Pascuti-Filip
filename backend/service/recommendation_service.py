import math
import torch
import torchaudio
import os
import ai_model

from fastapi import HTTPException, UploadFile

from domain.user import User
import repo
from sqlalchemy.orm import Session


class RecommendationService:

    def convert_vectorization_string_to_list(self, vectorization_string: str):
        result = []
        for value in vectorization_string.strip().split(","):
            result.append(float(value))
        return result

    def convert_vectorization_list_to_string(self, vectorization):
        result = ""
        for value in vectorization:
            result += str(round(value, 3)) + ","
        return result[:-1]

    def get_recommendations_for_user(self, current_user: User, db: Session):
        if not current_user.vectorization or not current_user.cluster:
            raise HTTPException(status_code=400, detail="Vectorization is not present")

        print(f"current user is: {current_user.username}")

        users_in_cluster = repo.user_repo.get_all_from_cluster(db, cluster=current_user.cluster)

        current_user_vectorization = self.convert_vectorization_string_to_list(current_user.vectorization)

        users_in_cluster = [user for user in users_in_cluster if user.username != current_user.username]

        users_in_cluster.sort(key=lambda x: math.dist(self.convert_vectorization_string_to_list(x.vectorization),
                                                      current_user_vectorization))

        for user in users_in_cluster:
            print(user.username)

        return users_in_cluster[:5]

    async def assign_vecotorization_to_user(self, db: Session, current_user: User, upload_file: UploadFile,
                                            kmeans) -> User:
        vectorization = await self.get_user_vectorization_from_file(upload_file)
        cluster = self.get_cluster(kmeans, vectorization)
        vectorization_string = self.convert_vectorization_list_to_string(vectorization)

        updated_user = repo.user_repo.update(db, user_in=current_user, vectorization=vectorization_string,
                                             cluster=cluster)

        return updated_user

    def get_cluster(self, kmeans, vectorization):
        cluster = kmeans.predict([vectorization])
        return int(cluster[0])

    async def get_user_vectorization_from_file(self, file: UploadFile):
        filename = file.filename
        with open(filename, "wb") as write_file:
            content = await file.read()
            write_file.write(content)
        input_tensor, _ = torchaudio.load(filename)
        vectorization = self.get_vectorization_list(ai_model.model, input_tensor)
        os.remove(filename)

        return vectorization

    def get_vectorization_list(self, model, input_tensor):
        with torch.no_grad():
            model.eval()
            predictions = model(input_tensor)
            vectorization = [0.0] * 50
            for elem in predictions.tolist():
                for index, value in enumerate(elem):
                    vectorization[index] += value
            for index, value in enumerate(vectorization):
                vectorization[index] = value / len(predictions)
            return vectorization


user_service = RecommendationService()
