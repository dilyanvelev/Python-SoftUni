from project.hero import Hero
from unittest import TestCase, main


class HeroTests(TestCase):
    def setUp(self):
        self.hero = Hero('TestUsername', 1, 100, 100)
        self.enemy = Hero('TestEnemy', 1, 50, 50)

    def test_initialization(self):
        self.assertEqual('TestUsername', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_enemy_name_is_equal_username_raise_exception(self):
        self.enemy.username = 'TestUsername'
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_if_health_is_negative_or_zero_raise_valueError(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_enemy_if_health_is_negative_or_zero_raise_valueError(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight TestEnemy. He needs to rest", str(ve.exception))

    def test_health_remove_after_fight(self):
        self.hero.health = 50
        self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(-50, self.enemy.health)

    def test_return_draw_after_fight(self):
        self.hero.health = 50
        self.assertEqual('Draw', self.hero.battle(self.enemy))

    def test_hero_win(self):
        self.hero.battle(self.enemy)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_hero_win_return_you_win(self):
        self.assertEqual('You win', self.hero.battle(self.enemy))

    def test_enemy_win(self):
        self.enemy.health = 110
        self.enemy.damage = 110
        self.hero.battle(self.enemy)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(15, self.enemy.health)
        self.assertEqual(115, self.enemy.damage)

    def test_enemy_win_return_you_lose(self):
        self.enemy.health = 110
        self.enemy.damage = 110
        self.assertEqual('You lose', self.hero.battle(self.enemy))

    def test__str__(self):
        self.assertEqual("Hero TestUsername: 1 lvl\n" \
                         "Health: 100\n" \
                         "Damage: 100\n", str(self.hero))


if __name__ == '__main__':
    main()
