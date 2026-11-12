class Moderator:
    def __init__(self, name):
        self.name = name

    def get_permissions(self):
        return f"Предоставлен доступ к: чтению, изменению, удалению модератору - {self.name}."
