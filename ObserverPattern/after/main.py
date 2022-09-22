from api.slack_listener import setup_slack_event_handlers
from api.log_listener import setup_log_listeners
from api.email_listener import setup_email_listeners
from api.plan import upgrade_plan
from api.user import register_new_user, password_forgotten

setup_email_listeners()
setup_log_listeners()
setup_slack_event_handlers()

register_new_user("KeyboardSyntax", "awesome69Password", "spam@nicheart.me")

password_forgotten("spam@nicheart.me")

upgrade_plan("spam@nicheart.me")