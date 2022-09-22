from .event import subscribe
from lib.email import send_email


def handle_user_registered_event(user):
    send_email(user.username, user.email,
               f"Welcome {user.username}",
               f"Thanks for registering, {user.username}!\nRegards, The Dev Team")


def handle_user_password_forgotten_event(user):
    send_email(user.username, user.email,
               "Reset your password",
               f"To Reset your password, use this very secure code: {user.reset_code}\nRegards, The Dev Team")


def handle_plan_upgraded_event(user):
    send_email(user.username, user.email,
               "Thank You",
               f"Thank you for upgrading, {user.username}! You're going to love it. \nregards, The Dev Team")


def setup_email_listeners():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("user_password_forgotten", handle_user_password_forgotten_event)
    subscribe("plan_upgraded", handle_plan_upgraded_event)
