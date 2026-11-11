class Admin:
    def __init__(self, name):
        self.name = name

    def get_permissions(self):
        return f"Предоставлен доступ администратору {self.name}"
