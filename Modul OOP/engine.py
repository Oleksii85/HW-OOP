import models
import settings
import exceptions


def get_player_name() -> str:
    name = ''
    while name == '':
        name = input("ENTER YOUR NAME: ").strip()
    return name


def play() -> None:
    name = get_player_name()
    player = models.Player(name)
    enemy = models.Enemy(settings.INITIAL_ENEMY_LEVEL)
    while True:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except exceptions.EnemyDown:
            player.score += settings.SCORE_ENEMY_DOWN
            print(f'Enemy level {enemy.level} is defeated')
            enemy = models.Enemy(enemy.level + 1)
        except exceptions.GameOver:
            with open("scores.txt", "a") as f:
                f.write(name)
                f.write(f', your scores = {str(player.score)}')
                f.close()
            break
    print(f'{name} is defeated \nSCORE POINTS: {player.score} \n \nGOOD BYE ')


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        print('GAME OVER')
