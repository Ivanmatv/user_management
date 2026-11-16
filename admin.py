from user import User
from moderator import Moderator


class Admin(User):
    def __init__(self, name):
        super().__init__(name)
        self.__name: str = name
        self.__moderators: set = set()

    def get_permissions(self) -> str:
        return f"Предоставлен доступ к администратору - {self.__name}."

    def add_moderator(self, moderator: Moderator) -> None:
        if isinstance(moderator, Moderator):
            self.__moderators.add(moderator)

    def get_moderators(self) -> str:
        return ", ".join(self.__moderators)

    def remove_moderator(self, moderator: Moderator) -> None:
        if isinstance(moderator, Moderator) and moderator in self.__moderators:
            self.__moderators.remove(moderator)
