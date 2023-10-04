class User:
    def __init__(self, name_id, username):
        self.name_id = name_id
        self.username = username
        self.books = []

    def info(self):
        return f"{', '.join(sorted(self.books))}"

    def __str__(self):
        return f"{self.name_id}, {self.username}, {self.books}"
