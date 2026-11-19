from user import User


class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.__name: str = name

    def get_permissions(self) -> list:
        return ["add_moderator", "get_moderators", "remove_moderator"]
