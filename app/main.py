from fastapi import FastAPI
from .quotes import quotes

app = FastAPI()

@app.get('/')
def quotes_text(topic:str | None="motivational"):
    data = quotes(topic)
    return data