from api.plan import upgrade_plan
from api.user import register_new_user, password_forgotten

register_new_user("KeyboardSyntax", "awesome69Password", "spam@nicheart.me")

password_forgotten("spam@nicheart.me")

upgrade_plan("spam@nicheart.me")