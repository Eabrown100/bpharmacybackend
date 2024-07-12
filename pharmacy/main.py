from contextlib import asynccontextmanager
from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from pharmacy.database.core import Base, SessionMaker, engine
from pharmacy.routers import users, inventories, admins

import sqlalchemy


@asynccontextmanager
async def lifespan(app: FastAPI):

    #Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(inventories.router)
app.include_router(users.router)
app.include_router(admins.router)

origins=[
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://127.0.0.1:5500",
    "http://127.0.0.1:5501",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/ping")
def ping_pong() -> dict[str, str]:
    return {"message": "pong"}

@app.get("/name/{first_name}")
def get_first_name(first_name: str) -> dict[str, str]:
    return {"name": first_name}

@app.post("/name")
def get_surname(surname: str = Body(embed=True)) -> dict[str, str]:
    return {"surname": surname}

