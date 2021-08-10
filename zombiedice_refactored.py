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
        self._tutorial = None

    def display_instructions(self):
        if self._tutorial:
            self._tutorial = False
        elif self._tutorial is None:
            answer = ''
            while answer.lower() not in ('y', 'yes', 'n', 'no'):
                answer = input('Are you new to Zombie Dice?: (y/n) ')
                if answer.lower() in ('y', 'yes'):
                    self._tutorial = True
                elif answer.lower() in ('n', 'no'):
                    self._tutorial = False
                else:
                    continue
        else:
            pass
    
    def update_dice_counters(self):
        self._remaining_dice_counter = Counter(self._remianing_dice)
        self._current_dice_counter = Counter(self._remaining_dice_counter)
    
    def print_current_dice(self):
        for color, count in self._current_dice_counter:
            cprint(f'{count} {color} {(lambda count: "die" if count == 1 else "dice")(count)}', color)
            time.sleep(0.25)

    def print_remaining_dice(self):
        for color, count in self._remaining_dice_counter:
            cprint(f'{count} {color} {(lambda count: "die" if count == 1 else "dice")(count)}', color)
            time.sleep(0.25)

    def roll_all_dice(self):
        for index, die in enumerate(self._current_dice):
            die.roll()
            if die._last_roll == 'shotgun':
                self._shotgun_count += 1
                background_color = 'on_red'
            elif die._last_roll == 'brains':
                self._brain_count += 1
                background_color = 'on_blue'
            else:
                background_color = None
            cprint(f'{ordinal(index + 1)} {die._color} die rolled ', end = '')
            cprint(f'{die._last_roll}', on_color = background_color)
            time.sleep(1)

    def take_turn(self):
        # Update game state
        self._roll_number += 1
        while len(self._current_dice) < 3:
            self._current_dice.append(self._remaining_dice[random.randint(0, len(self._remaining_dice) - 1)])
        self.update_dice_counters()

        # Update the player
        print('Here we go!')
        time.sleep(0.75)
        print(f'This is your {ordinal(self._roll_number)} roll this round.')
        time.sleep(0.75)
        print('You\'re rolling:')
        time.sleep(0.25)
        self.print_current_dice()

        # Rolling the dice
        time.sleep(1) 
        print('\nYou rolled', end = '')
        for i in range(4):
            print('.', end = '')
            time.sleep(0.5)
        print(' ')
        self.roll_all_dice()