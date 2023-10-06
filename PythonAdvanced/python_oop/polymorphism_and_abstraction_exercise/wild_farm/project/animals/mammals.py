from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    # TODO:__init__?
    def make_sound(self):
        return "Squeak"

    @property
    def food_that_eats(self):
        return [Vegetable, Fruit]

    @property
    def gained_weight(self):
        return 0.10


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.40


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    @property
    def gained_weight(self):
        return 0.30

    @property
    def food_that_eats(self):
        return [Vegetable, Meat]


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    @property
    def gained_weight(self):
        return 1.00

    @property
    def food_that_eats(self):
        return [Meat]
