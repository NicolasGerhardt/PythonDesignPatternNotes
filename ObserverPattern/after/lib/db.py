from dataclasses import dataclass
import email
from pydoc import plain
from typing import List
from venv import create


users = []


@dataclass
class User:
    username: str
    password: str
    email: str
    plain: str = "basic"
    reset_code: str = ""

    def reset_password(self, code: str, new_password: str):
        if (code != self.reset_code):
            raise Exception("Invalid password reset code")
        self.password = new_password
        self.reset_code = ""


def create_user(username: str, password: str, email: str) -> User:
    print(f"DB: creating user database entry for {username} ({email}).")
    new_user = User(username, password, email)
    users.append(new_user)
    return new_user


def find_user(email: str) -> User:
    for user in users:
        if user.email == email:
            return user
    raise Exception(f"user with email address {email} not found.")
