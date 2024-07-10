
from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder
from app.main import app
from app.utils import Movie, generate_random_string

client = TestClient(app)

fake_movie: Movie = {
    "id": 1,
    "title": "Avatar",
    "overview": "Is a 2009 science fiction film directed by James Cameron. Set in the mid-22nd century, it follows paraplegic ex-Marine Jake Sully who infiltrates the Na'vi, an alien species on the planet Pandora",
    "year": "2009",
    "rating": 7.8,
    "category": "Action",
}


def test_root() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Welcome to My Movie App - API"}


def test_create_movie() -> None:
    response = client.post(
        "/movies/",
        json=fake_movie
    )
    assert response.status_code == 200
    data = jsonable_encoder(response.json())
    assert len(data) == 1
    assert fake_movie["id"] == data[0]["id"]

def test_get_movies() -> None:
    response = client.get(
        "/movies"
    )

    assert response.status_code == 200
    data = jsonable_encoder(response.json())
    assert len(data) == 1
    assert fake_movie["id"] == data[0]["id"]

def test_get_movies_by_id() -> None:
    movie_id:int = 1
    response = client.get(
        f"/movies/{movie_id}"
    )
    assert response.status_code == 200
    data = jsonable_encoder(response.json())
    assert fake_movie["id"] == data["id"]

def test_get_movies_by_category() -> None:
    movie_category:str = "Action"
    response = client.get(
        f"/movies/?category={movie_category}"
    )
    assert response.status_code == 200
    data = jsonable_encoder(response.json())
    assert len(data) == 1
    assert fake_movie["id"] == data[0]["id"]

def test_edit_movie() -> None:
    movie_id: int = 1
    new_title = generate_random_string(15)
    updated_movie: Movie = fake_movie
    updated_movie["title"] = new_title
    response = client.put(
        f"/movies/?id={movie_id}",
        json=updated_movie
    )
    assert response.status_code == 200
    data = jsonable_encoder(response.json())
    assert new_title == data[0]["title"]

def test_remove_movie() -> None:
    movie_id:int = 1
    response = client.delete(
        f"/movies/?id={movie_id}"
    )
    assert response.status_code == 200
    data = jsonable_encoder(response.json())
    assert len(data) == 0