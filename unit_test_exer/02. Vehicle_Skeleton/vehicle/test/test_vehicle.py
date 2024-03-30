from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.vehicle = Vehicle(
            100,
            100
        )

    def test_correct_init(self):
        self.assertEqual(100, self.vehicle.fuel)
        self.assertEqual(100, self.vehicle.capacity)
        self.assertEqual(100, self.vehicle.horse_power)
        self.assertEqual(self.vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_if_default_fuel_consumption_is_correct(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_not_enough_fuel_raises_excepiton(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_when_enought_fuel(self):
        self.vehicle.drive(50)
        self.assertEqual(self.vehicle.fuel, 37.5)

    def test_too_much_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(500)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_refuels_correct_sum(self):
        self.vehicle.fuel = 50
        self.vehicle.refuel(20)

        self.assertEqual(70, self.vehicle.fuel)

    def test_str_returns_correct_string(self):
        expected_result = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(self.vehicle.__str__(), expected_result)


if __name__ == '__main__':
    main()