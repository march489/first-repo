#!/usr/bin/env python3
""" zombiedice_3.py --
    This simulates playing the Zombie Dice game. 
    See the rules online for how to play.
    
    Version 1.1.3:
    This version of the game just simulates rolling dice
    for one round, checking win conditions, and telling you 
    how many points you scored that round. """

import random
import time
# from termcolor import cprint
from collections import Counter

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

class ZombieDie:
    def __init__(self, color):
        self.color = color
        self.last_roll = None

        if self.color == 'red':
            self.faces = ['footsteps'] * 2 + ['brains'] + ['shotgun'] * 3
        elif self.color == 'green':
            self.faces = ['footsteps'] * 2 + ['brains'] * 3 + ['shotgun']
        else:
            self.faces = ['footsteps'] * 2 + ['brains'] * 2 + ['shotgun'] * 2

    def roll(self):
        self.last_roll = random.choice(self.faces)
        return self.last_roll

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class RoundState:
    def __init__(self, round_number: int, player: Player):
        self.remaining_dice = [
            ZombieDie('green'), ZombieDie('green'), ZombieDie('green'),
            ZombieDie('green'), ZombieDie('green'), ZombieDie('green'),
            ZombieDie('yellow'), ZombieDie('yellow'), ZombieDie('yellow'),
            ZombieDie('yellow'), ZombieDie('red'), ZombieDie('red'), 
            ZombieDie('red')
            ]
        self.current_dice = []
        self.brain_count = 0
        self.shotgun_count = 0

class Instructions:
    def __init__(self, on: bool):
        if on:
            self.run_tutorial = True
        else: 
            self.run_tutorial = False

class Game:
    def get_players(self):
        all_aboard = False
        unique_name = True
        while not all_aboard:
            new_player_name = input(f'What is Player {len(self.player_list) + 1}\'s name? ')
            try:
                self.check_unique_name(new_player_name)
                self.player_list.append(Player(new_player_name))
            except ValueError:
                print('Someone with that name is already playing.')
                time.sleep(0.25)
                print('Please choose another name.')
                continue
            more_players = ''
            while not more_players:
                more_players = input('Is anyone else playing? (y/n): ')
                if more_players not in ('yes', 'y', 'no', 'n'):
                    continue
                elif more_players in ('no', 'n'):
                    all_aboard = True
                else:
                    break

    def check_unique_name(self, name):
        for player in self.player_list:
            if name == player.name:
                raise ValueError
            else:
                pass

    def __init__(self):
        self.player_list = []
        self.round_number = 0
        self.get_players()

# if __name__ == '__main__':
#     Game()