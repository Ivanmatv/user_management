from admin import Admin
from moderator import Moderator


admin = Admin("Пётр")
moderator = Moderator("Игорь")

admin_class = Admin
moderator_class = Moderator


def is_permission_allowed(person, allowed_class) -> bool:
    if isinstance(person, allowed_class):
        print(person.get_permissions())
        return True
    else:
        print("Доступ запрещён!")
        return False


is_permission_allowed(person=admin, allowed_class=admin_class)
is_permission_allowed(person=moderator, allowed_class=admin_class)
