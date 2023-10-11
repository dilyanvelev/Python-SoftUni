from project.mammal import Mammal
from unittest import TestCase, main


class MammalTest(TestCase):
    def setUp(self):
        self.mammal = Mammal("Pinko", "dog", 'woof')

    def test_initialization(self):
        self.assertEqual("Pinko", self.mammal.name)
        self.assertEqual('dog', self.mammal.type)
        self.assertEqual('woof', self.mammal.sound)

    def test_make_correct_sound(self):
        self.assertEqual('Pinko makes woof', self.mammal.make_sound())

    def test_get_correct_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_info_method(self):
        self.assertEqual('Pinko is of type dog', self.mammal.info())


if __name__ == '__main__':
    main()
