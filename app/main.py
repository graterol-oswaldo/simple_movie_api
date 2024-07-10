from fastapi import FastAPI
from .routes import router
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "my-movie-api"
app.version = "0.0.1"
app.include_router(router)


@app.get("/", tags=["home"])
def main() -> HTMLResponse:
    return {"msg": "Welcome to My Movie App - API"}
