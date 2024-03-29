from unittest import TestCase, main
from project.mammal import Mammal
class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal(
            "cathy",
            'cat',
            'meow'
        )

    def test_correct_init(self):
        self.assertEqual('cathy', self.mammal.name)
        self.assertEqual('cat', self.mammal.type)
        self.assertEqual('meow', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)


    def test_get_sound_returns_correct_string(self):
        self.assertEqual('cathy makes meow', self.mammal.make_sound())

    def test_get_kingdom_returns_animals(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_get_info_returns_correct_str(self):
        self.assertEqual('cathy is of type cat', self.mammal.info())

if __name__ == '__main__':
    main()