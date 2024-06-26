from fastapi import FastAPI

app = FastAPI()

@app.get('/health-check')
async def hello():
    return "Hello !!!"