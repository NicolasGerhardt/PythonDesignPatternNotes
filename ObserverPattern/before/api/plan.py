
from lib.email import send_email
from lib.log import log
from lib.slack import post_slack_message
from lib.db import find_user


def upgrade_plan(email:str):
    user = find_user(email)

    user.plan = "paid"

    post_slack_message("sales",
        f"{user.username} has upgraded thier plan")

    send_email(user.username, user.email,
        "Thank You",
        f"Thank you for upgrading, {user.username}! You're going to love it. \nregards, The Dev Team")

    log(f"User with email address {user.email} has upgraded their plan")