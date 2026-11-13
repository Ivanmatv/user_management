class Admin:
    def __init__(self, name):
        self.name = name

    def get_permissions(self) -> str:
        return (
            f"Предоставлен доступ к:"
            f" добавлению, чтению, обновлению, удалению "
            f"администратору - {self.name}."
        )
