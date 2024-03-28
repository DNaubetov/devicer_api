import uvicorn
from fastapi import FastAPI
from database.connection import Settings
from routes.computer import computers_router
from ip import get_local_ip
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await settings.initialize_database()
    yield


app = FastAPI(lifespan=lifespan, title="Devices system", version="1")

settings = Settings()

app.include_router(computers_router, prefix="/computers")


# uvicorn main:app --host 192.168.137.215 --port 8000 --reload


@app.get("/")
async def root():
    return "Hellow, World!"


if __name__ == "__main__":
    if get_local_ip():
        uvicorn.run("main:app", host=get_local_ip(), port=8000, reload=True, workers=3)
    uvicorn.run("main:app", host='127.0.0.1', port=8000)
