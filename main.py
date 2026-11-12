from user import User
from admin import Admin
from moderator import Moderator

user = User("Иван")
admin = Admin("Пётр")
moderator = Moderator("Игорь")

allowed_class = Admin

def is_permission_allowed(person, allowed_type) -> None:
    if isinstance(person, allowed_type):
        print(person.get_permissions())
    else:
        print("Доступ запрещён!")


is_permission_allowed(person=user, allowed_type=allowed_class)
is_permission_allowed(person=admin, allowed_type=allowed_class)
