class User:
    def __init__(self, name):
        self.name = name

    def get_permissions(self) -> str:
        return f"Предоставлен доступ к: чтению пользователю - {self.name}."
