
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from app.main import app
from app.utils import Movie, User, generate_random_string
from app.jwt_manager import create_token

client = TestClient(app)


fake_user: User = {
    "email": "admin@mymovieapi.lcl",
    "password": "asdf1234"
}

fake_movie: Movie = {
    "id": 4,
    "title": "Avatar",
    "overview": "Is a 2009 science fiction film directed by James Cameron. Set in the mid-22nd century, it follows paraplegic ex-Marine Jake Sully who infiltrates the Na'vi, an alien species on the planet Pandora",
    "year": 2009,
    "rating": 7.8,
    "category": "Action",
}


def test_login_success() -> None:
    response = client.post(
        "/login",
        json=fake_user)
    assert response.status_code == 200


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


def test_create_movie() -> None:
    response = client.post(
        "/movies/",
        json=fake_movie
    )
    assert response.status_code == 201
    assert response.json() == {"msg": "The movie was created"}


def test_get_movies() -> None:
    token: str = create_token(fake_user)
    headers={
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
    movie_id: int = 4
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
