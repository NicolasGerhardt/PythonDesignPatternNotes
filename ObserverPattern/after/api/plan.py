from .event import post_event
from lib.db import find_user


def upgrade_plan(email: str):
    user = find_user(email)

    user.plan = "paid"

    post_event("plan_upgraded", user)
