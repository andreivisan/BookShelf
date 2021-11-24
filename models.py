from typing import Optional, List
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum


class Tag(BaseModel):
    id: Optional[UUID] = uuid4()
    label: str


class Note(BaseModel):
    id: Optional[UUID] = uuid4()
    label: str


class Book(BaseModel):
    id: Optional[UUID] = uuid4()
    title: str
    read_date: str
    tags: List[Tag]
    notes: List[Note]


class Role(str, Enum):
    admin = "admin"
    user = "user"


class User(BaseModel):
    id: Optional[UUID] = uuid4()
    name: str
    username: str
    email: str
    password: str
    roles: List[Role]
    #books: List[Book]
    #roles: List[Role]


class UserUpdateRequest(BaseModel):
    name: Optional[str]
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]
    roles: Optional[List[Role]]
