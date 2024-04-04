from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation
class TestRailwayStation(TestCase):

    def setUp(self):
        self.railway = RailwayStation('Patnicheski')

    def test_correct_init(self):
        self.assertEqual(self.railway.name, 'Patnicheski')
        self.assertEqual(self.railway.arrival_trains, deque())
        self.assertEqual(self.railway.departure_trains, deque())

    def name_less_or_equal_than_three_raises_ve(self):
        with self.assertRaises(ValueError) as ve:
            self.railway.name = 'da'

        self.assertEqual("Name should be more than 3 symbols!",
                         str(ve.exception))

    def test_new_arrival_appends_the_train_info_correctly(self):
        self.railway.new_arrival_on_board('Train8')
        self.assertEqual('Train8', *self.railway.arrival_trains)

    def test_train_has_arrived_when_no_arrival_trains(self):
        self.assertEqual(len(self.railway.arrival_trains), 0)

        self.railway.arrival_trains.append('BGD')
        self.assertNotEqual(self.railway.arrival_trains[0], 'ODS')

        result = self.railway.train_has_arrived('BDG')
        self.assertEqual(result,
                         f"There are other trains to arrive before BDG.")

        self.railway.departure_trains.append(self.railway.arrival_trains.popleft())
        self.assertEqual(len(self.railway.arrival_trains), 0)
        self.assertEqual(len(self.railway.departure_trains), 1)
        self.assertEqual(self.railway.departure_trains[0], 'BGD')

        self.railway.arrival_trains.append('Varna-Sofia')
        self.assertEqual(f"Varna-Sofia is on the platform and will leave in 5 minutes.",
                         self.railway.train_has_arrived('Varna-Sofia'))

    def test_train_returns_error_if_others_are_arriving_first(self):
        self.railway.arrival_trains.append('VarnaSofia')
        self.railway.departure_trains.append('BGD')

        self.assertEqual(f"There are other trains to arrive before BGD.",
                         self.railway.train_has_arrived('BGD'))

        self.assertEqual(len(self.railway.departure_trains), 1)
        self.assertEqual(self.railway.departure_trains[0], 'BGD')
        self.railway.departure_trains.popleft()
        self.assertEqual(len(self.railway.departure_trains), 0)

        self.railway.departure_trains.append('BGD')
        self.assertEqual(self.railway.train_has_left('BGD'), True)

    def test_train_return_false_when_no_trains(self):
        self.assertEqual(len(self.railway.departure_trains), 0)
        self.assertEqual(False, self.railway.train_has_left('BDG'))

    def test_train_return_false_when_other_trains_are_first(self):
        self.railway.departure_trains.append('GGG')
        self.assertNotEqual(self.railway.departure_trains[0], 'BDG')
        self.assertEqual(False, self.railway.train_has_left('BDG'))


if __name__ == "__main__":
    main()