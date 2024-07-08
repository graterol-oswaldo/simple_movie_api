from fastapi import FastAPI
from .routes import router
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "my-movie-api"
app.version = "0.0.1"
app.include_router(router)


@app.get("/", tags=["home"])
def message() -> HTMLResponse:
    return HTMLResponse("<h1>Welcome to My Movie App - API</h1>")


