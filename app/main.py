from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Dict
from middlewares.error_handler import ErrorHandler
from routers.user import user_router
from routers.movie import movie_router


app = FastAPI()
app.title = "my-movie-api"
app.version = "0.0.1"
app.include_router(user_router)
app.include_router(movie_router)
app.add_middleware(ErrorHandler)

@app.get("/", tags=["home"], response_model=Dict, status_code=200)
def main() -> Dict:
    return JSONResponse(content={"msg": "Welcome to My Movie App - API"}, status_code=200)

