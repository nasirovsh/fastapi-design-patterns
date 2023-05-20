from fastapi import FastAPI
from typing import List
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str


class UserRepository:
    def get_users(self) -> List[User]:
        # Fetch users from the data storage and return them
        pass


app = FastAPI()
user_repository = UserRepository()


@app.get("/users")
def get_users():
    users = user_repository.get_users()
    return users
