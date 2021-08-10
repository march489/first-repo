#!/usr/bin/env python3
""" zombiedice_refactored.py --
    This simulates playing the Zombie Dice game. 
    See the rules online for how to play.
    
    Version 1.1.2:
    This version of the game just simulates rolling dice
    for one round, checking win conditions, and telling you 
    how many points you scored that round. """

import random
import time
from termcolor import cprint
from collections import Counter

class ZombieDie:
    def __init__(self, color):
        self._color = color
        self._last_roll = None

        if self._color == 'red':
            self._faces = ['footsteps'] * 2 + ['brains'] + ['shotgun'] * 3
        elif self._color == 'green':
            self._faces = ['footsteps'] * 2 + ['brains'] * 3 + ['shotgun']
        else:
            self._faces = ['footsteps'] * 2 + ['brains'] * 2 + ['shotgun'] * 2

    # This is mostly for debugging. 
    def __repr__(self):
        return f'{self._color.title()} Die'
    
    def roll(self):
        self._last_roll = random.choice(self._faces)
        return self._last_roll

    def get_last_roll(self):
        return self._last_roll

# Stolen -- turns numbers into their ordinal, e.g. ordinal(3) --> '3rd'   
ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n//10%10!=1)*(n%10<4)*n%10::4])

class RoundState:
    def __init__(self):
        self._remianing_dice = [ZombieDie('green'), ZombieDie('green'), ZombieDie('green'), 
            ZombieDie('green'), ZombieDie('green'), ZombieDie('green'), ZombieDie('red'), 
            ZombieDie('red'), ZombieDie('red'), ZombieDie('yellow'), ZombieDie('yellow'), 
            ZombieDie('yellow'), ZombieDie('yellow')]
        self._remaining_dice_counter = Counter(self._remianing_dice)
        self._current_dice = []
        self._current_dice_counter = Counter(self._remaining_dice_counter)
        self._shotgun_count = 0
        self._brain_count = 0
        self._roll_number = 0
        self._new_round = True
        self._tutorial = False

    def got_shot(self):
        self._shotgun_count += 1
    
    def eat_brains(self):
        self._brain_count += 1

    def stop_playing(self):
        self._new_round = False

    def display_instructions(self):
        if self._tutorial:
            self._tutorial = False
            return None
        answer = ''
        while answer.lower() not in ('y', 'yes', 'n', 'no'):
            answer = input('Are you new to Zombie Dice?: (y/n) ')
            if answer.lower() in ('y', 'yes'):
                self._tutorial = True            

    def take_turn(self):
        self._roll_number += 1
        while len(self._current_dice) < 3:
            self._current_dice.append(self._remaining_dice[random.randint(0, len(self._remaining_dice) - 1)])
        print('Here we go!')
        
