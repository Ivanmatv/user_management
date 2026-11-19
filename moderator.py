from user import User


class Moderator(User):
    def __init__(self, name):
        super().__init__(name)
        self.__name: str = name

    def get_permissions(self) -> list:
        return ["post", "write_post", "delete_post", "update_post"]
