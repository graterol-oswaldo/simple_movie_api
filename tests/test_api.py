
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from app.main import app
from .utils import generate_random_string
from utils.jwt_manager import create_token
from schemas.movie import Movie
from schemas.user import User,UserBase

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from config.database import Base
from routers.main import get_db

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)



def test_create_user() -> None:
    user: User = User(name="Test User",email="test@domain.lcl",password="asdf1234")
    response = client.post(
        "/users/",
        json=user.model_dump()
    )
    assert response.status_code == 201, response.text
    assert response.json() == {"msg": "The user was created"}



def test_login_success() -> None:
    user: User = UserBase(email="test@domain.lcl",password="asdf1234")
    response = client.post(
        "/login",
        json=user.model_dump())
    assert response.status_code == 200

"""
def test_login_failed() -> None:
    data: User = {
        "email": "usuario@dominio.test",
        "password": "A(w%BeX<<7I=(P4_T9ZVZy@LE"
    }
    response = client.post(
        "/login",
        json=data)
    assert response.status_code == 401


def test_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to My Movie App - API"}

"""


def test_create_movie() -> None:
    movie: Movie = Movie(title="Inception", overview="A skilled thief is given a chance to erase his criminal record by infiltrating dreams and planting an idea into the target's subconscious.",
                         year=2010, rating=7.2, category="Science Fiction")
    response = client.post(
        "/movies/",
        json=movie.model_dump()
    )
    assert response.status_code == 201, response.text
    assert response.json() == {"msg": "The movie was created"}


""""
def test_get_movies() -> None:
    token: str = create_token(fake_user)
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = client.get(
        "/movies",
        headers=headers
    )

    assert response.status_code == 200
    data = jsonable_encoder(response.json())
    assert len(data) == 4
    assert fake_movie["id"] == data[3]["id"]

def test_get_movies_by_id() -> None:
    movie_id: int = 1
    response = client.get(
        f"/movies/{movie_id}"
    )
    assert response.status_code == 200
    data = jsonable_encoder(response.json())
    assert fake_movie["id"] == data["id"]

def test_get_error_if_movies_id_not_exist() -> None:
    movie_id: int = 555
    response = client.get(
        f"/movies/{movie_id}"
    )
    assert response.status_code == 404


def test_get_movies_by_category() -> None:
    movie_category: str = "Action"
    response = client.get(
        f"/movies/?category={movie_category}"
    )
    assert response.status_code == 200
    data = jsonable_encoder(response.json())
    assert len(data) == 1
    assert fake_movie["id"] == data[0]["id"]


def test_get_error_if_movie_category_not_exist() -> None:
    movie_category: str = "AABBCCDD"
    response = client.get(
        f"/movies/?category={movie_category}"
    )
    assert response.status_code == 404


def test_edit_movie() -> None:
    movie_id: int = 4
    new_title = generate_random_string(15)
    updated_movie: Movie = fake_movie
    updated_movie["title"] = new_title
    response = client.put(
        f"/movies/?id={movie_id}",
        json=updated_movie
    )
    assert response.status_code == 200
    assert response.json() == {"msg": "The movie was updated"}


def test_remove_movie() -> None:
    movie_id: int = 4
    response = client.delete(
        f"/movies/?id={movie_id}"
    )
    assert response.status_code == 200
    assert response.json() == {"msg": "The movie was removed"}
"""
