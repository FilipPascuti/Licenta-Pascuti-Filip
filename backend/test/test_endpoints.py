import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.base_class import Base
from domain import User
from main import app
from api.deps import get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


@pytest.fixture()
def test_db():
    Base.metadata.create_all(bind=engine)
    insert_values_in_db()
    yield
    Base.metadata.drop_all(bind=engine)


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def insert_values_in_db():
    db = next(override_get_db())
    users = [
        User(
            username="doru",
            fullname="doru_full",
            hashed_password="$2b$12$3K4ylfBaS9Ljg6NZxnFH9ekGVb9DfcyCrO551sqWOJXQDslBp7c5i",
        ),
        User(
            username="marian",
            fullname="marian",
            hashed_password="$2b$12$c56Fk6it.IMSh85QRIbvm.3t7XPds9tF60ZXhsfutkAtz8mBKlvI.",
            vectorization="0.003,0.011,0.005,0.002,0.406,0.002,0.0,0.0,0.0,0.0,0.0,0.001,0.075,0.0,0.004,0.003,0.0,0.005,0.0,0.001,0.0,0.0,0.007,0.018,0.0,0.001,0.001,0.009,0.001,0.003,0.0,0.004,0.004,0.001,0.004,0.0,0.0,0.0,0.0,0.125,0.002,0.0,0.024,0.001,0.001,0.002,0.059,0.0,0.001,0.0",
            cluster=53
        ),
        User(
            username="dorian",
            fullname="dorian",
            hashed_password="$2b$12$qeQ/OameyzvhrQz.NimlPeO60PFjUf0lPDY5NGTTFM2w8nz4VHcCK",
            vectorization="0.003,0.011,0.005,0.002,0.406,0.002,0.0,0.0,0.0,0.0,0.0,0.001,0.075,0.0,0.004,0.003,0.0,0.005,0.0,0.001,0.0,0.0,0.007,0.018,0.0,0.001,0.001,0.009,0.001,0.003,0.0,0.004,0.004,0.001,0.004,0.0,0.0,0.0,0.0,0.125,0.002,0.0,0.024,0.001,0.001,0.002,0.059,0.0,0.001,0.0",
            cluster=53
        ),
        User(
            username="falik@gmail.com",
            fullname="Falik",
            hashed_password="$2b$12$82axplYQkl9s40Hyj3PKh.EjOGmpkimTX8NTcJsdh0XABGHw0HYkG",
            vectorization="0.012,0.007,0.006,0.009,0.509,0.003,0.0,0.026,0.0,0.002,0.001,0.001,0.037,0.0,0.005,0.001,0.001,0.002,0.001,0.002,0.0,0.0,0.031,0.058,0.0,0.0,0.007,0.001,0.009,0.09,0.005,0.006,0.002,0.0,0.003,0.0,0.005,0.013,0.004,0.041,0.001,0.0,0.05,0.001,0.003,0.013,0.145,0.003,0.002,0.0",
            cluster=53
        ),
        User(
            username="ammonite@gmail.com",
            fullname="Ammonite",
            hashed_password="$2b$12$IzAoY63hoTjrW6aEV6LyQujZavM41WTAzJZlLrCkx.xcHDAYlnDwC",
            vectorization="0.029,0.092,0.038,0.088,0.509,0.004,0.001,0.02,0.001,0.005,0.005,0.003,0.068,0.0,0.007,0.012,0.0,0.004,0.0,0.0,0.0,0.002,0.102,0.046,0.0,0.0,0.007,0.0,0.001,0.024,0.002,0.01,0.005,0.008,0.003,0.0,0.005,0.009,0.0,0.191,0.007,0.001,0.03,0.001,0.001,0.003,0.02,0.001,0.0,0.0",
            cluster=53
        ),
        User(
            username="selfdelusion@gmail.com",
            fullname="Self Delusion",
            hashed_password="$2b$12$dMY8QQTqNfzZnT8Heg1oROPc/CU7btXFofgaMiSyI93RCkMQa3iYa",
            vectorization="0.021,0.096,0.046,0.036,0.428,0.021,0.001,0.009,0.006,0.004,0.004,0.007,0.056,0.0,0.007,0.005,0.001,0.041,0.0,0.001,0.001,0.0,0.095,0.075,0.0,0.0,0.012,0.005,0.002,0.009,0.001,0.007,0.005,0.002,0.014,0.0,0.002,0.072,0.001,0.004,0.013,0.0,0.008,0.009,0.06,0.02,0.062,0.0,0.003,0.0",
            cluster=53
        ),
        User(
            username="emma'smini@gmail.com",
            fullname="Emma's Mini",
            hashed_password="$2b$12$RSGLJIEe87C.1PXg4.iUD.1fn8PberE8RzC/Wqwlb9WW8wu8jBQjC",
            vectorization="0.02,0.082,0.074,0.027,0.504,0.004,0.0,0.007,0.003,0.001,0.003,0.009,0.033,0.0,0.013,0.002,0.0,0.036,0.0,0.001,0.001,0.0,0.071,0.011,0.0,0.0,0.019,0.006,0.001,0.019,0.001,0.008,0.004,0.001,0.001,0.0,0.008,0.016,0.0,0.007,0.078,0.0,0.001,0.027,0.005,0.002,0.138,0.001,0.0,0.0",
            cluster=53
        ),
    ]

    db.add_all(users)
    db.commit()


def test_register(test_db):
    register_data = {
        "username": "ani",
        "fullname": "ani_full",
        "password": "ani_pass",
    }
    response = client.post("/api/auth/register", json=register_data)
    assert response.status_code == 200
    assert response.json()["username"] == "ani"
    assert response.json()["fullname"] == "ani_full"
    assert response.json()["id"] == 8


def login_user(username, password):
    response = client.post("/api/auth/login", data={
        "username": username,
        "password": password
    })
    token = response.json()["access_token"]

    return token


def get_simple_auth_header(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    return headers


def get_auth_header_with_content_type(token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    return headers


def test_login(test_db):
    response = client.post("/api/auth/login", data={
        "username": "doru",
        "password": "doru_pass"
    })
    tokens = response.json()
    assert response.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]


def test_get_current_user_details(test_db):
    headers = get_auth_header_with_content_type(login_user("doru", "doru_pass"))

    response = client.get("/api/user/details", headers=headers)
    user_dict = response.json()
    print(user_dict)
    assert user_dict["username"] == "doru"
    assert user_dict["fullname"] == "doru_full"


def test_upload_characteristic_file(test_db):
    headers = get_simple_auth_header(login_user("doru", "doru_pass"))

    with open("./ring trimmed 8s.mp3", "rb") as file:
        response = client.post("/api/user/characterization", headers=headers,
                               files={"upload_file": file})
        user_dict = response.json()
        print(user_dict)
        assert response.status_code == 200
        assert user_dict["username"] == "doru"
        assert user_dict[
                   "vectorization"] == "0.003,0.011,0.005,0.002,0.406,0.002,0.0,0.0,0.0,0.0,0.0,0.001,0.075,0.0,0.004,0.003,0.0,0.005,0.0,0.001,0.0,0.0,0.007,0.018,0.0,0.001,0.001,0.009,0.001,0.003,0.0,0.004,0.004,0.001,0.004,0.0,0.0,0.0,0.0,0.125,0.002,0.0,0.024,0.001,0.001,0.002,0.059,0.0,0.001,0.0"
        assert user_dict["cluster"] == 53


def test_get_recommendations(test_db):
    headers = get_auth_header_with_content_type(login_user("marian", "marian"))

    response = client.get("api/user/recommendation", headers=headers)
    result = response.json()
    assert response.status_code == 200
    assert len(result) == 5
    assert result[0]["fullname"] == "dorian"
    assert result[1]["fullname"] == "Falik"
    assert result[2]["fullname"] == "Ammonite"
    assert result[3]["fullname"] == "Self Delusion"
    assert result[4]["fullname"] == "Emma's Mini"
