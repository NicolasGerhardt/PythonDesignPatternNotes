from .event import post_event
from lib.stringtools import get_random_string
from lib.db import create_user, find_user


def register_new_user(username: str, password: str, email: str):
    user = create_user(username, password, email)

    post_event("user_registered", user)


def password_forgotten(email:str):
    user = find_user(email)

    user.reset_code = get_random_string(16)

    post_event("user_password_forgotten", user)