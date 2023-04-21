import random
import exceptions
import settings


class Enemy:

    def __init__(self, level: int = 1) -> None:
        self.level: int = level                              # рівень противника
        self.health: int = settings.INITIAL_ENEMY_LEVEL      # очки здоров’я противника

    def decrease_health(self) -> None:
        self.health -= 1
        if self.health < 1:
            raise exceptions.EnemyDown

    @staticmethod
    def select_attack() -> int:
        return random.randint(1, 3)                   # KNIGHT - 1, THIEF - 2, WIZARD - 3

    @staticmethod
    def select_defence() -> int:
        return random.randint(1, 3)                   # KNIGHT - 1, THIEF - 2, WIZARD - 3


class Player:

    def __init__(self, name: str) -> None:
        self.name: str = name
        self.health: int = settings.INITIAL_PLAYER_NAME
        self.score: int = 0
        self.fight_result: str = ''

    def decrease_health(self) -> None:
        self.health -= 1
        if self.health < 1:
            raise exceptions.GameOver

    def attack(self, enemy: Enemy) -> None:
        sel_attack = self.select_attack()
        sel_defence = enemy.select_defence()
        res_fight = self.fight(sel_attack, sel_defence)
        if res_fight == '+':
            print('YOUR ATTACK IS SUCCESSFUL!')
            self.score += settings.SCORE_SUCCESS_ATTACK
            enemy.decrease_health()
        elif res_fight == 'draw':
            print('IT’S A DRAW!')
        else:
            print('YOUR ATTACK IS FAILED!')

    def defence(self, enemy: Enemy) -> None:
        sel_defence = self.select_defence()
        sel_attack = enemy.select_attack()
        res_fight = self.fight(sel_attack, sel_defence)
        if res_fight == '+':
            print('YOUR DEFENCE IS SUCCESSFUL!')
        elif res_fight == 'draw':
            print('IT’S A DRAW!')
        else:
            print('YOUR DEFENCE IS FAILED!')
            self.decrease_health()

    def fight(self, attack, defence) -> str:                   # KNIGHT - 1, THIEF - 2, WIZARD - 3
        if attack == 1 and defence == 2 or attack == 2 and defence == 3 or attack == 3 and defence == 1:
            self.fight_result = '+'
            return self.fight_result
        elif attack == defence:
            self.fight_result = 'draw'
            return self.fight_result
        else:
            self.fight_result = '-'
            return self.fight_result

    @staticmethod
    def select_attack() -> int:
        select = 0
        while select not in ('1', '2', '3'):
            select = input('MAKE A FIGHT CHOICE FROM (KNIGHT - 1, THIEF - 2, WIZARD - 3): ')
        return int(select)

    @staticmethod
    def select_defence() -> int:
        select = 0
        while select not in (1, 2, 3):
            try:
                select = int(input('MAKE A FIGHT CHOICE FROM (KNIGHT - 1, THIEF - 2, WIZARD - 3): '))
            except ValueError:
                pass
        return select
