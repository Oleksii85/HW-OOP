import models
import settings
scores = open('scores.txt', 'w')


def get_player_name() -> str:
    name = (input("ENTER YOUR NAME: ")).strip()
    while name == '':
        print("Player name cannot be an empty string")
        get_player_name()
    return name


def play() -> None:
    level = settings.INITIAL_ENEMY_LEVEL
    name = get_player_name()
    scores.write(name)
    player = models.Player(name)
    enemy = models.Enemy(level)
    while player.health != 0:
        player.attack(enemy)
        if enemy.health < 1:
            print(f'Enemy level {enemy.level} is defeated')
            enemy.level += 1
            player.score += settings.SCORE_ENEMY_DOWN
        else:
            player.defence(enemy)
            if enemy.health < 1:
                print(f'Enemy level {enemy.level} is defeated')
                enemy.level += 1
                player.score += settings.SCORE_ENEMY_DOWN
            else:
                continue
    scores.write(f', your scores = {str(player.score)}')
    print(f'{name} is defeated \nSCORE POINTS: {player.score} \n \nGOOD BYE ')
    scores.close()


play()
