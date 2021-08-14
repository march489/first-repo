import sys
from unittest.mock import patch
from unittest import TestCase

def get_input(text):
    return input(text)

def answer():
    ans = get_input('enter yes or no')
    if ans == 'yes':
        return 'you entered yes'
    else:
        return 'you entered no'

class Test(TestCase):
    # get_input will return 'yes' during this test
    @patch('zombiedice_3_test.get_input', return_value = 'yes')
    def test_answer_yes(self, input):
        self.assertEqual(answer(), 'you entered yes')

# from unittest import mock
# from unittest import TestCase
# import unittest
# from zombiedice_3 import Game

# class ZombieDiceTest(TestCase):
#     @mock.patch('zombiedice_3.Game.input', create = True)
#     def test_players_added_to_player_list(self, mocked_input):
#         Game()
#         Game.get_players()
#         mocked_input.side_effect = ['Marcello', 'yes', 'Madison', 'no']
#         result = Game.player_list
#         self.assertEqual(result, ['Marcello', 'Madison'])

#     def assertRaisesWithMessage(self, exception):
#         return self.assertRaisesRegex(exception, r".+")
  
# if __name__ == '__main__':
#     unittest.main()
