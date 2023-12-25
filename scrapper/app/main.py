from fastapi import FastAPI

app = FastAPI()

@app.get('/quotes')
def quotes(topic:str | None="motivational"):
    return {}