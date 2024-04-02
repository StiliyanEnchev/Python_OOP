from unittest import TestCase, main
from project.climbing_robot import ClimbingRobot


class TestClimbingRobot(TestCase):
    ALLOWED_CATEGORIES = ['Mountain', 'Alpine', 'Indoor', 'Bouldering']

    def setUp(self):

        self.chucky = ClimbingRobot('Indoor',
                                    "Type_part",
                                    100,
                                    50
                                    )

        self.robot_with_softwares = ClimbingRobot('Indoor',
                                                  "Type_part",
                                                  100,
                                                  50)

        self.robot_with_softwares.installed_software = [
            {"name": "Pycharm", 'capacity_consumption': 20, 'memory_consumption': 40}
        ]

    def test_check_correct_init(self):
        self.assertEqual(self.chucky.category, 'Indoor')
        self.assertEqual(self.chucky.part_type, 'Type_part')
        self.assertEqual(self.chucky.capacity, 100)
        self.assertEqual(self.chucky.memory, 50)
        self.assertEqual([], self.chucky.installed_software)


    def test_if_category_raises_value_error_when_it_is_not_one_of_the_given_one(self):
        with self.assertRaises(ValueError) as ve:
            self.chucky.category = 'Bobabot'

        self.assertEqual(f"Category should be one of {self.ALLOWED_CATEGORIES}",
                         str(ve.exception))

    def test_get_used_capacity_returns_the_correct_sum(self):
        expected_result = self.robot_with_softwares.get_used_capacity()
        result = sum(s['capacity_consumption'] for s in self.robot_with_softwares.installed_software)

        self.assertEqual(expected_result, result)


    def test_get_available_capacity_returns_the_correct_sum(self):
        result = self.robot_with_softwares.get_available_capacity()
        expected_result = self.robot_with_softwares.capacity - sum(s['capacity_consumption']
                                                                   for s in self.robot_with_softwares.installed_software)
        self.assertEqual(result, expected_result)


    def test_get_used_memory_returns_the_correct_sum(self):

        expected_result = self.robot_with_softwares.get_used_memory()
        result = sum(s['memory_consumption'] for s in self.robot_with_softwares.installed_software)
        self.assertEqual(expected_result, result)

    def test_get_available_memory_returns_the_correct_sum(self):
        result = self.robot_with_softwares.get_available_memory()
        expected_result = self.robot_with_softwares.memory - sum(s['memory_consumption']
                                                                 for s in self.robot_with_softwares.installed_software)

        self.assertEqual(result, expected_result)

    def test_install_software_with_max_capacity_taken(self):
        result = self.chucky.install_software({'name': 'PyCharm',
                                               'memory_consumption': 50,
                                               'capacity_consumption': 100})

        self.assertEqual(result, f"Software 'PyCharm' successfully installed on Indoor part.")

        self.assertEqual(self.chucky.installed_software, [{'name': 'PyCharm',
                                                           'memory_consumption': 50,
                                                           'capacity_consumption': 100}])

    def test_install_software_with_left_capacity_afterwards(self):
        result = self.chucky.install_software(
            {'name': 'PyCharm', 'memory_consumption': 25, 'capacity_consumption': 50}
        )

        self.assertEqual(result, f"Software 'PyCharm' successfully installed on Indoor part.")
        self.assertEqual(self.chucky.installed_software,
                         [{'name': 'PyCharm', 'memory_consumption': 25, 'capacity_consumption': 50}])

    def test_install_software_with_one_requirement_higher_return_error_message(self):
        result = self.chucky.install_software({'name': 'PyCharm', 'memory_consumption': 50, 'capacity_consumption': 400})
        self.assertEqual(result, f"Software 'PyCharm' cannot be installed on Indoor part.")
        self.assertEqual(self.chucky.installed_software,
                         []
                         )

    def test_install_software_with_too_much_requirements_return_error_message(self):
        result = self.chucky.install_software({'name': 'PyCharm', 'memory_consumption': 200, 'capacity_consumption': 400})
        self.assertEqual(result, f"Software 'PyCharm' cannot be installed on Indoor part.")
        self.assertEqual(self.chucky.installed_software,
                         []
                         )
if __name__ == "__main__":
    main()


