from fastapi import APIRouter, Body, Depends, Path, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.movie import Movie
from typing import List, Dict
from sqlalchemy.orm import Session
from config.database import Base, engine
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from routers.main import get_db

movie_router = APIRouter()

Base.metadata.create_all(bind=engine)


@movie_router.get("/movies", tags=["movies"], response_model=List, status_code=200, dependencies=[Depends(JWTBearer())])
def get_movies(db:Session = Depends(get_db)) -> List:
    result = MovieService(db).get_movies()
    if not result:
        return JSONResponse(content={"msg": "No movie records"}, status_code=200)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.get("/movies/{id}", tags=["movies"], response_model=Dict, status_code=200)
def get_movies(id: int = Path(ge=1, le=2000), db:Session = Depends(get_db)) -> Dict:
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(content={"msg": f"There is no any movie record with the id: {id}"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.get("/movies/", tags=["movies"], response_model=List, status_code=200)
def get_movies_by_category(category: str = Query(min_length=5, max_length=150), db:Session = Depends(get_db)) -> List:
    result = MovieService(db).get_movie_by_category(category)
    if not result:
        return JSONResponse(content={"msg": f"There is no any movie record with the category: {category}"}, status_code=404)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.post("/movies/", tags=["movies"], response_model=Dict, status_code=201)
def create_movie(movie: Movie = Body(), db: Session = Depends(get_db)) -> Dict:
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"msg": "The movie was created"}, status_code=201)


@movie_router.put("/movies/", tags=["movies"], response_model=Dict, status_code=200)
def edit_movie(id: int, movie: Movie = Body(), db:Session=Depends(get_db)) -> Dict:
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(content={"msg": f"There is no any movie record with the id: {id}"}, status_code=200)
    MovieService(db).update_movie(id, movie)
    return JSONResponse(content={"msg": "The movie was updated"}, status_code=200)


@movie_router.delete("/movies/", tags=["movies"], response_model=Dict, status_code=200)
def delete_movie(id: int, db:Session=Depends(get_db)) -> Dict:
    result = MovieService(db).get_movie_by_id(id)
    if not result:
        return JSONResponse(content={"msg": f"There is no any movie record with the id: {id}"}, status_code=200)
    MovieService(db).delete_movie(id)
    return JSONResponse(content={"msg": "The movie was removed"}, status_code=200)
