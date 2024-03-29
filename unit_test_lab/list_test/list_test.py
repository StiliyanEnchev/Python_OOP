from unittest import TestCase, main

from unit_test_lab.list_test.list import IntegerList


class TestIntegerList(TestCase):

    def setUp(self):
        self.i_list = IntegerList(5.5, 1, 2, 3, 'hello')

    def test_correct_init_ignores_non_int_values(self):
        self.assertEqual([1, 2, 3], self.i_list.get_data())

    def test_add_non_int_el_to_list_raises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.i_list.add(5.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_int_to_the_list(self):
        self.i_list.add(5)
        self.assertEqual(5, self.i_list.get_data()[-1])

    def test_remove_index_with_out_of_range_index_raises_index_error(self):

        with self.assertRaises(IndexError) as ie:
            self.i_list.remove_index(1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_remove_valid_index(self):
        self.i_list.remove_index(0)

        self.assertEqual([2, 3], self.i_list.get_data())


    def test_get_with_out_of_range_index(self):

        with self.assertRaises(IndexError) as ie:
            self.i_list.get(1000)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_with_valid_index_return_value_on_index(self):
        result = self.i_list.get(2)
        self.assertEqual(3, result)

    def test_insert_on_invalid_index_raises_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.i_list.insert(1000, 5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_insert_on_valid_index_but_not_integer_type_raises_value_error(self):

        with self.assertRaises(ValueError) as ve:
            self.i_list.insert(1, 6.5)

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_valid_inserted_integer_on_valid_index(self):
        expected_list = self.i_list.get_data().copy()
        expected_list.insert(1, 5)
        self.i_list.insert(1, 5)


        self.assertEqual(expected_list, self.i_list.get_data())

    def test_get_biggest_el(self):
        self.assertEqual(3, self.i_list.get_biggest())

    def test_get_index(self):
        result = self.i_list.get_index(1)
        self.assertEqual(0, result)

if __name__ == "__main__":
    main()