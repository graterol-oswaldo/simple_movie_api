from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from typing import TypedDict

app = FastAPI()
app.title = "my-movie-api"
app.version = "0.0.1"


class Movie(TypedDict):
    id: int
    title: str
    overview: str
    year: int
    rating: float
    category: str


movies: list[Movie] = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
]


@app.get("/", tags=["home"])
def message() -> HTMLResponse:
    return HTMLResponse("<h1>Hello World!</h1>")


@app.get("/movies", tags=["movies"])
def get_movies() -> list:
    return movies


@app.get("/movies/{id}", tags=["movies"])
def get_movies(id: int) -> dict:
    movie: dict = next((movie for movie in movies if movie["id"] == id), {})
    return movie


@app.get("/movies/", tags=["movies"])
def get_movies_by_category(category: str) -> list:
    movies_by_category: list = [
        movie for movie in movies if movie.get("category") == category
    ]
    return movies_by_category


@app.post("/movies/", tags=["movies"])
def create_movie(movie: Movie = Body()) -> list[Movie]:
    movies.append(movie)
    return movies


@app.put("/movies/", tags=["movies"])
def edit_movie(id:int, new_movie: Movie) -> list[Movie]:
    position: int = next(
        (index for index, movie in enumerate(movies) if movie["id"] == id), -1
    )
    if position == -1:
        return []
    movies.pop(position)
    movies.insert(position, new_movie)
    return movies


@app.delete("/movies/", tags=["movies"])
def delete_movie(id: int, movie_to_delete: Movie) -> list[Movie]:
    position: int = next(
        (index for index, movie in enumerate(movies) if movie["id"] == id), -1
    )
    if position == -1:
        return []
    movies.pop(position)
    return movies
