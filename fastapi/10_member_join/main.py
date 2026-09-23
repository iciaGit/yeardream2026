from fastapi import FastAPI
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

app = FastAPI()

app.mount("/view", StaticFiles(directory="view"))

@app.get("/")
def main():
    return RedirectResponse("/view/index.html")