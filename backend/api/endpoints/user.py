from typing import Any

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from fastapi import Depends, UploadFile, File
from sqlalchemy.orm import Session

from api import deps

import dto
import domain
import service

router = InferringRouter()


@cbv(router)
class RecommendationController:
    db: Session = Depends(deps.get_db)
    current_user: domain.User = Depends(deps.get_current_user)

    @router.get("/details", response_model=dto.UserDetails)
    def get_current_user_details(
            self
    ) -> Any:
        return dto.UserDetails(
            username=self.current_user.username,
            fullname=self.current_user.fullname,
            vectorization=self.current_user.vectorization,
            cluster=self.current_user.cluster
        )

    @router.get("/recommendation")
    async def get_recommendations(
            self
    ):
        recommendations = service.user_service.get_recommendations_for_user(self.current_user, self.db)
        recommendations_dto = []

        for user in recommendations:
            recommendations_dto.append(
                dto.UserDetails(
                    username=user.username,
                    fullname=user.fullname,
                    vectorization=user.vectorization,
                    cluster=user.cluster
                )
            )

        return recommendations_dto

    @router.post("/characterization")
    async def upload_characteristic_file(
            self,
            kmeans=Depends(deps.get_kmeans_model),
            upload_file: UploadFile = File(...)
    ):
        updated_user = await service.user_service.assign_vecotorization_to_user(self.db, self.current_user, upload_file,
                                                                                kmeans)

        return dto.UserDetails(
            username=updated_user.username,
            fullname=updated_user.fullname,
            vectorization=updated_user.vectorization,
            cluster=updated_user.cluster
        )
