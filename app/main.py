from fastapi import FastAPI, Request
from pydantic import BaseModel
from model.model_kish import predict_kish
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
#app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="../app/templates")

class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    language: str


@app.get("/")
def home():
    return {"health_check": "OK"}

@app.get("/kish")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/convert")
async def convert_text(request: Request):
    data = await request.json()
    text = data.get('text', '')
    converted_text = predict_kish(text)  
    return {'convertedText': converted_text}

