#!/usr/bin/env python3
""" zombiedice.py --
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

    def __repr__(self):
        return f'Player: {self.name}'

class TurnState:
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
        # Gets the names of the people playing the game, adds them to the player list
        all_aboard = False
        while not all_aboard:
            new_player_name = input(f'What is Player {len(self.player_list)+ 1}\'s name? ')
            if self.check_valid_name(new_player_name):
                self.player_list.append(Player(new_player_name.strip()))
                self.player_name_list.append(new_player_name.lower().strip())
            else:
                print(' ')
                time.sleep(0.5)
                print(f'Error: That name is already taken. Please choose a unique name.' + '\n')
                continue

            more_people = ''
            while more_people.lower() not in ('y', 'yes', 'n', 'no'):
                more_people = input('Does anyone else want to play? (y/n): ')
                if more_people.lower() in ('n', 'no'):
                    all_aboard = True
                    print('Great! Let\'s get started!')
                    break
                elif more_people.lower() in ('y', 'yes'):
                    print('The more the merrier!')
                    break
                else:
                    continue

    def check_valid_name(self, potential_name: str):
        # Checks if the name just input is valid
        tmp = potential_name.lower().strip()
        for player_name in self.player_name_list:
            if tmp == player_name:
                return False
        return True

    

    def __init__(self):
        self.round_number = 0
        self.active_player = 0
        self.player_list = []
        self.player_name_list = []
        
