from fastapi import APIRouter, Body, Path, Query
from fastapi.responses import JSONResponse
from .utils import Movie, User, movies
from typing import List, Dict
from .jwt_manager import create_token

router = APIRouter()


@router.post("/login", tags=["auth"], response_model=Dict, status_code=200)
def login(user: User) -> Dict:
    admin_user: User = User(email="admin@mymovieapi.lcl", password="asdf1234")
    if user.email == admin_user.email and admin_user.password == admin_user.password:
        token: str = create_token(dict(user))
        return JSONResponse(content=token, status_code=200)
    return JSONResponse(content={"msg": "Invalid username or password"}, status_code=401)


@router.get("/", tags=["home"], response_model=Dict, status_code=200)
def main() -> Dict:
    return JSONResponse(content={"msg": "Welcome to My Movie App - API"}, status_code=200)


@router.get("/movies", tags=["movies"], response_model=List, status_code=200)
def get_movies() -> List:
    return JSONResponse(content=movies, status_code=200)


@router.get("/movies/{id}", tags=["movies"], response_model=Dict, status_code=200)
def get_movies(id: int = Path(ge=1, le=2000)) -> Dict:
    status_code: int = 200
    movie: Movie = next((movie for movie in movies if movie["id"] == id), {})
    if not movie:
        status_code = 404
    return JSONResponse(content=movie, status_code=status_code)


@router.get("/movies/", tags=["movies"], response_model=List, status_code=200)
def get_movies_by_category(category: str = Query(min_length=5, max_length=150)) -> List:
    status_code: int = 200
    movies_by_category: list = [
        movie for movie in movies if movie["category"] == category
    ]
    if not movies_by_category:
        status_code = 404
    return JSONResponse(content=movies_by_category, status_code=status_code)


@router.post("/movies/", tags=["movies"], response_model=Dict, status_code=201)
def create_movie(movie: Movie = Body()) -> Dict:
    movies.append(movie.model_dump())
    return JSONResponse(content={"msg": "The movie was created"}, status_code=201)


@router.put("/movies/", tags=["movies"], response_model=Dict, status_code=200)
def edit_movie(id: int, new_movie: Movie = Body()) -> Dict:
    status_code: int = 200
    for movie in movies:
        if movie["id"] == id:
            movie["title"] = new_movie.title
            movie["overview"] = new_movie.overview
            movie["year"] = new_movie.year
            movie["rating"] = new_movie.rating
            movie["category"] = new_movie.category
            return JSONResponse(content={"msg": "The movie was updated"}, status_code=status_code)
    status_code = 404
    return JSONResponse(content={"msg": f"Any movie found with {id}"}, status_code=status_code)


@router.delete("/movies/", tags=["movies"], response_model=Dict, status_code=200)
def delete_movie(id: int) -> Dict:
    status_code: int = 200
    position: int = next(
        (index for index, movie in enumerate(movies) if movie["id"] == id), -1
    )
    if position == -1:
        status_code = 404
        return JSONResponse(content={"msg": f"Any movie found with {id}"}, status_code=status_code)
    movies.pop(position)
    return JSONResponse(content={"msg": "The movie was removed"}, status_code=status_code)
