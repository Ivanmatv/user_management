class User:
    def __init__(self, name):
        self.name = name

    def get_permissions(self):
        return f"Предоставлен доступ пользователю {self.name}"
