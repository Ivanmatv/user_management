class User:
    def __init__(self, name):
        self.__name: str = name

    def get_permissions(self) -> list:
        return ["post", "edit", "delete", "get"]
