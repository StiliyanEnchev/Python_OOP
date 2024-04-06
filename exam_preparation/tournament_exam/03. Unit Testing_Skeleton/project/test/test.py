from unittest import TestCase, main
from project.trip import Trip

class TestTrip(TestCase):
    DESTINATION_PRICES_PER_PERSON = {
                                     'New Zealand': 7500,
                                     'Australia': 5700,
                                     'Brazil': 6200,
                                     'Bulgaria': 500
                                     }

    def setUp(self):
        self.trip_without_family = Trip(2500, 1, False)
        self.trip_with_family = Trip(5000, 3, True)

    def test_correct_init(self):
        self.assertEqual(self.trip_without_family.budget, 2500)
        self.assertEqual(self.trip_without_family.travelers, 1)
        self.assertEqual(self.trip_without_family.is_family, False)
        self.assertEqual(self.trip_without_family.booked_destinations_paid_amounts, {})

    def test_travellers_setter_raises_value_error_if_traveller_quantity_less_than_one(self):

        with self.assertRaises(ValueError) as ve:
            self.trip_without_family.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_if_destination_not_in_the_selected_ones_returns_correct_message(self):
        result = self.trip_without_family.book_a_trip('Bangladesh')
        self.assertEqual(result, 'This destination is not in our offers, please choose a new one!')

    def test_if_is_family_price_change(self):
        budget = self.trip_with_family.budget
        self.trip_with_family.book_a_trip('Bulgaria')
        price_paid = self.DESTINATION_PRICES_PER_PERSON['Bulgaria'] * 0.9
        end_price = budget - price_paid
        self.assertEqual(end_price, 4550)

    def test_correct_return_for_family_when_budget_lower_than_price(self):
        self.trip_without_family.budget = 0
        result = self.trip_without_family.book_a_trip('Bulgaria')
        self.assertEqual(result, 'Your budget is not enough!')

    def test_for_best_case_of_book_trip_that_is_successfull_removes_destination_price_from_the_budget_and_returns_correct_return(self):
        result = self.trip_without_family.book_a_trip('Bulgaria')
        self.assertEqual(result, 'Successfully booked destination Bulgaria! Your budget left is 2000.00')
        self.assertEqual(self.trip_without_family.budget, 2000)
        self.assertEqual(len(self.trip_without_family.booked_destinations_paid_amounts), 1)
        self.assertEqual(self.trip_without_family.booked_destinations_paid_amounts, {'Bulgaria': 500})
    def test_no_booked_destinations_correct_return(self):
        result = self.trip_without_family.booking_status()
        self.assertEqual(result, f'No bookings yet. Budget: 2500.00')

    def test_result_for_booking_status_when_there_are_such(self):
        self.trip_without_family.budget = 10000
        self.trip_without_family.book_a_trip('Bulgaria')
        self.trip_without_family.book_a_trip('Australia')
        result = self.trip_without_family.booking_status()
        expected_result = (f'Booked Destination: Australia\n'
                           f'Paid Amount: 5700.00\n'
                           f'Booked Destination: Bulgaria\n'
                           f'Paid Amount: 500.00\n'
                           f'Number of Travelers: 1\n'
                           f'Budget Left: 3800.00')

        self.assertEqual(result, expected_result)
        result = sorted(self.trip_without_family.booked_destinations_paid_amounts.items())
        self.assertEqual(result,
                         [('Australia', 5700), ('Bulgaria', 500)])

    def test_family_setter_if_it_returns_false_when_trying_to_set_to_true_on_less_than_two_travellers(self):
        self.trip_without_family.is_family = True
        self.assertEqual(self.trip_without_family.is_family, False)


if __name__ == '__main__':
    main()