import sys
import threading
import unittest
import pytest

from zombiedice_3 import *


class ZombieDiceTest(unittest.TestCase):
    def players_added_to_player_list(self):
        Game.get_players()
        'Marcello'
        'Meg'
        'Carly'
        'Madison'
        return self.assertEqual(Game.player_list == ['Marcello', 'Meg', 'Carly', 'Madison'])
        
    # Utility functions
    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")

if __name__ == '__main__':
    unittest.main()
