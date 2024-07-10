from fastapi import APIRouter, Body
from .utils import Movie, movies

router = APIRouter()

@router.get("/movies", tags=["movies"])
def get_movies() -> list:
    return movies


@router.get("/movies/{id}", tags=["movies"])
def get_movies(id: int) -> Movie:
    movie: Movie = next((movie for movie in movies if movie.id == id), {})
    return movie


@router.get("/movies/", tags=["movies"])
def get_movies_by_category(category: str) -> list:
    movies_by_category: list = [
        movie for movie in movies if movie.category == category
    ]
    return movies_by_category


@router.post("/movies/", tags=["movies"])
def create_movie(movie: Movie = Body()) -> list[Movie]:
    movies.append(movie)
    return movies


@router.put("/movies/", tags=["movies"])
def edit_movie(id: int, new_movie: Movie = Body()) -> list[Movie]:
    for movie in movies:
        if movie.id == id:
            movie.title = new_movie.title
            movie.overview = new_movie.overview
            movie.year = new_movie.year
            movie.rating = new_movie.rating
            movie.category = new_movie.category
            return movies
    return []


@router.delete("/movies/", tags=["movies"])
def delete_movie(id: int) -> list[Movie]:
    position: int = next(
        (index for index, movie in enumerate(movies) if movie.id == id), -1
    )
    if position == -1:
        return []
    movies.pop(position)
    return movies
