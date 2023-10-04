class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"


car1 = Car("Kia", "Rio", "1.3L B3 I4")
car2 = Car("Kia", "Rio 2021", "2.3L B3 I4")
print(car1.get_info())
print(car2.get_info())
