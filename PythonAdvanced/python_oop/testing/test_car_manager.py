class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


# car = Car("a", "b", 1, 4)
# car.make = ""
# print(car)

from unittest import TestCase, main


class CarTests(TestCase):
    def setUp(self):
        self.car = Car("Mercedes", "CLS", 10, 80)

    def test_wrong_make_setter_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = None
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_setter_setting_correct_value(self):
        self.assertEqual("Mercedes", self.car.make)

    def test_make_correct_property_return(self):
        self.assertEqual("Mercedes", self.car._Car__make)

    def test_wrong_model_setter_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = None
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_setter_setting_correct_value(self):
        self.assertEqual("CLS", self.car.model)

    def test_model_correct_property_return(self):
        self.assertEqual("CLS", self.car._Car__model)

    def test_wrong_fuel_consumption_set_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_correct_fuel_consumption_set(self):
        self.assertEqual(10, self.car.fuel_consumption)

    def test_correct_return_property_fuel_consumption(self):
        self.assertEqual(10, self.car._Car__fuel_consumption)

    def test_wrong_fuel_capacity_set_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_correct_fuel_capacity_set(self):
        self.assertEqual(80, self.car.fuel_capacity)

    def test_correct_return_property_fuel_capacity(self):
        self.assertEqual(80, self.car._Car__fuel_capacity)

    def test_wrong_setter_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_correct_setter_fuel_amount(self):
        self.assertEqual(0, self.car.fuel_amount)

    def correct_return_fuel_amount_property(self):
        self.assertEqual(0, self.car._Car__fuel_amount)

    def test_refuel_with_negative_or_zero_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_correct_refueling(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car._Car__fuel_amount)

    def test_prevent_overfilling_the_trunk(self):
        self.car.refuel(90)
        self.assertEqual(80, self.car._Car__fuel_amount)

    def test_cannot_drive_the_distance_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_can_drive_the_distance(self):
        self.car.fuel_amount = 2
        self.car.drive(10)
        self.assertEqual(1, self.car.fuel_amount)


if __name__ == '__main__':
    main()
