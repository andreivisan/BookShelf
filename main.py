from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException

from models import User, Role, UserUpdateRequest

app = FastAPI()

db: List[User] = [
    User(
        id=UUID("83fdcfa8-c9a1-4efb-a2e2-72b15a42a424"),
        name="Jamila Ahmed",
        username="jahmed",
        email="jamila.ahmed@test.com",
        password="secret",
        roles=[Role.user]
    ),
    User(
        id=UUID("51ca4a14-a53c-4a77-9eb0-1faab4fbe680"),
        name="John Doe",
        username="jdoe",
        email="john.doe@test.com",
        password="secret",
        roles=[Role.admin, Role.user]
    )
]


@app.get("/")
async def root():
    return {
        "Hello": "World"
    }


@app.get("/api/v1/users")
async def fetch_users():
    return db


@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}


@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )


@app.put("/api/v1/users/{user_id}")
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db:
        if user.id == user_id:
            if user_update.name is not None:
                user.name = user_update.name
            if user_update.username is not None:
                user.username = user_update.username
            if user_update.email is not None:
                user.email = user_update.email
            if user_update.password is not None:
                user.password = user_update.password
            if user_update.roles is not None:
                user.roles = user_update.roles
            return
    raise HTTPException(
        status_code=404,
        detail=f"user with id: {user_id} does not exists"
    )
