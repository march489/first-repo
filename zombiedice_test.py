import sys
from unittest.mock import patch
from unittest import TestCase
from zombiedice import *

if __name__ == '__main__':
    my_game = Game()
    my_game.get_players()
    print(my_game.players)
    