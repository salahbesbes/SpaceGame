from coreGame.gameBase import GameBase
from coreGame.objectBase import SpaceObject


if __name__ == '__main__':
    game = GameBase(800, 600)
    game.init_game()
    game.play_game()


