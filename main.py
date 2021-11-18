from typing import List
from uuid import uuid4
from fastapi import FastAPI

from models import User, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        name="Jamila Ahmed",
        username="jahmed",
        email="jamila.ahmed@test.com",
        password="secret",
        roles=[Role.user]
    ),
    User(
        id=uuid4(),
        name="John Doe",
        username="jdoe",
        email="john.doe@test.com",
        password="secret",
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
def root():
    return {
        "Hello": "World"
    }
