from unit_test_lab.car_manager.car_manager import Car
from unittest import TestCase, main

class TestCar(TestCase):
    def setUp(self):
        self.car = Car('Nissan', 'GTR', 10, 50)
    def test_correct_init(self):
        self.assertEqual('Nissan', self.car.make)
        self.assertEqual('GTR', self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)
    def test_if_make_raises_exep_without_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))
    def test_if_model_raises_exep_without_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))
    def test_fuel_consumption_with_zero_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))
    def test_fuel_capacity_with_zero_fuel_raise_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_if_fuel_amount_new_negative_value_raises_ex(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_zero_fuel_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_more_than_capacity_fills_to_capacity(self):
        self.car.refuel(80)
        self.car.fuel_capacity = 50

        self.assertEqual(50, self.car.fuel_capacity)

    def test_drive_car_without_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_car_with_fuel_decreases_it(self):
        self.car.refuel(1000)
        self.car.drive(10)

        self.assertEqual(49.0, self.car.fuel_amount)

if __name__ == "__main__":
    main()