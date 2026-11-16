from user import User


class Moderator(User):
    def __init__(self, name):
        super().__init__(name)
        self.__name: str = name
        self.__post_count: int = 0

    def get_permissions(self) -> str:
        return f"Предоставлен доступ модератору - {self.__name}."

    def post(self) -> None:
        self.__post_count += 1

    def get_post_count(self) -> int:
        return self.__post_count

    def delete_post(self) -> None:
        self.__post_count -= 1
