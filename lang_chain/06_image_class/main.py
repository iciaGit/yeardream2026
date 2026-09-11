import os.path

from fastapi import FastAPI, UploadFile
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from starlette.staticfiles import StaticFiles

from image_service import fileUpload, class_img

IMG_PATH = './upload'
app = FastAPI()
app.mount("/view",StaticFiles(directory="view"))

if not os.path.exists(IMG_PATH):
    os.makedirs(IMG_PATH)

app.add_middleware(CORSMiddleware,allow_origins=['*'], allow_methods=['*'])

@app.get("/")
def index():
    return RedirectResponse("/view/upload.html")

@app.post("/upload")
def upload(files:UploadFile):
    save_path = f'{IMG_PATH}/{files.filename}'
    msg = 'file upload 실패'
    result = None
    if fileUpload(files.file,save_path) == 1:
        msg = 'file upload 성공'
        result = class_img(save_path)

    return {"upload":msg,
            "image":files.filename,"result":result}






