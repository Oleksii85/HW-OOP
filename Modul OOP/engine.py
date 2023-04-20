import models
import settings
import exceptions


def get_player_name() -> str:
    name = ''
    while name == '':
        name = (input("ENTER YOUR NAME: ")).strip()
    return name


def play() -> None:
    level = settings.INITIAL_ENEMY_LEVEL
    name = get_player_name()
    scores = open('scores.txt', 'w')
    scores.write(name)
    player = models.Player(name)
    enemy = models.Enemy(level)
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except exceptions.EnemyDown:
            player.score += settings.SCORE_ENEMY_DOWN
            print(f'Enemy level {enemy.level} is defeated')
            enemy = models.Enemy(enemy.level + 1)
        except exceptions.GameOver:
            break
    scores.write(f', your scores = {str(player.score)}')
    print(f'{name} is defeated \nSCORE POINTS: {player.score} \n \nGOOD BYE ')
    scores.close()


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        print('GAME OVER')
