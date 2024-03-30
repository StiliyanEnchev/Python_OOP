from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Hero", 1, 100.50, 10.50)
        self.enemy = Hero("Enemy", 1, 50.50, 5.50)

    def test_for_correct_init(self):
        self.assertEqual("Hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100.50, self.hero.health)
        self.assertEqual(10.50, self.hero.damage)

    def test_both_names_the_same_in_battle_raises_exception(self):
        self.enemy.username = "Hero"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_no_health_raises_exception_during_battler(self):
        self.hero.health = 0
        expected_res = "Your health is lower than or equal to 0. You need to rest"
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_res, str(ve.exception))

    def test_enemy_no_health_raises_exception_during_battler(self):
        self.enemy.health = 0

        expected_res = f"You cannot fight {self.enemy.username}. He needs to rest"

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual(expected_res, str(ve.exception))

    def test_draw_battle_reduces_both_players_stats_and_returns_draw(self):
        self.hero.damage = 60.50
        self.enemy.damage = 100.50
        result = self.hero.battle(self.enemy)

        self.assertEqual('Draw', result)
        self.assertEqual(self.enemy.health, -10)
        self.assertEqual(self.hero.health, 0)

    def test_win_raise_stats(self):
        self.hero.damage = 60.50
        self.enemy.damage = 10
        result = self.hero.battle(self.enemy)

        self.assertEqual(result, 'You win')
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 95.50)
        self.assertEqual(self.hero.damage, 65.50)

    def test_loose_raise_enemy_stats(self):
        self.hero.damage = 10.50
        self.enemy.damage = 100.50
        result = self.hero.battle(self.enemy)

        self.assertEqual(result, 'You lose')
        self.assertEqual(self.enemy.level, 2)
        self.assertEqual(self.enemy.health, 45)
        self.assertEqual(self.enemy.damage, 105.50)

    def test_str_method_correct_return(self):
        result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
               f"Health: {self.hero.health}\n" \
               f"Damage: {self.hero.damage}\n"

        self.assertEqual(result, self.hero.__str__())


if __name__ == '__main__':
    main()







