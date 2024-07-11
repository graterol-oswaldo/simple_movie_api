from fastapi import FastAPI
from .routes import router

app = FastAPI()
app.title = "my-movie-api"
app.version = "0.0.1"
app.include_router(router)



