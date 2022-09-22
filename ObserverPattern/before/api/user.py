from lib.stringtools import get_random_string
from lib.log import log
from lib.email import send_email
from lib.slack import post_slack_message
from lib.db import create_user, find_user


def register_new_user(username: str, password: str, email: str):
    user = create_user(username, password, email)

    post_slack_message("sales", 
        f"{user.username} has registered wiht email address {user.email}. Please spam this person")

    send_email(user.username, user.email,
        f"Welcome {user.username}",
        f"Thanks for registering, {user.username}!\nRegards, The Dev Team")

    log(f"User registered with email address {user.email}")

def password_forgotten(email:str):
    user = find_user(email)

    user.reset_code = get_random_string(16)

    send_email(user.username, user.email,
        "Reset your password",
        f"To Reset your password, use this very secure code: {user.reset_code}\nRegards, The Dev Team")

    log(f"User with email address {user.email} requested a password reset")