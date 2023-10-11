from project.vehicle import Vehicle
from unittest import TestCase, main


class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(20.5, 175.5)

    def test_class_attribute_default_fuel_consumption(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_initializing(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(175.5, self.vehicle.horse_power)
        self.assertEqual(20.5, self.vehicle.capacity)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_cannot_drive_kilometers_not_enough_fuel_raise_exception(self):
        self.vehicle.fuel = 0
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_can_drive_kilometers_have_enough_fuel(self):
        self.vehicle.drive(1)
        self.assertEqual(19.25, self.vehicle.fuel)

    def test_refueling_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refueling_if_fuel_less_than_fuel_capacity(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(10)
        self.assertEqual(18, self.vehicle.fuel)

    def test__str__(self):
        expected_str = "The vehicle has 175.5 " \
                       "horse power with 20.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected_str, str(self.vehicle))


if __name__ == '__main__':
    main()
