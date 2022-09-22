from lib.slack import post_slack_message
from .event import subscribe


def handle_user_registered_event(user):
    post_slack_message("sales",
                       f"{user.username} has registered wiht email address {user.email}. Please spam this person")


def handle_user_upgraded_event(user):
    post_slack_message("sales",
                       f"{user.username} has upgraded thier plan")


def setup_slack_event_handlers():
    subscribe("user_registered", handle_user_registered_event)
    subscribe("plan_upgraded", handle_user_upgraded_event)
