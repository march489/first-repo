#!/usr/bin/env python3
""" zombiedice_script.py --
    This simulates playing the Zombie Dice game. 
    See the rules online for how to play.
    
    Version 1.1.1:
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

dice_list = [ZombieDie('green'), ZombieDie('green'), ZombieDie('green'), ZombieDie('green'), 
             ZombieDie('green'), ZombieDie('green'), ZombieDie('red'), ZombieDie('red'),
             ZombieDie('red'), ZombieDie('yellow'), ZombieDie('yellow'), ZombieDie('yellow'),
             ZombieDie('yellow')]
shotgun_count = 0
brain_count = 0
current_dice =[]
roll_number = 0
new_round = True

# Start the game
print('\n    Start of round    \n----------------------')
cprint('\nWelcome to ZOMBIE DICE!', 'red')
time.sleep(0.5)

while new_round: 
    roll_number += 1
    while len(current_dice) < 3:        
        # guarantees you roll three dice
        current_dice.append(dice_list.pop(random.randint(0,len(dice_list) - 1))) 

    # Start the round
    print('Here we go!')
    time.sleep(0.75)
    dice_counter = Counter([die._color for die in current_dice])
    print(f'This is your {ordinal(roll_number)} roll this round.')
    time.sleep(0.75)
    print('You\'re rolling:')
    time.sleep(0.25)
    for color, count in dice_counter.items():
        cprint(f'{count} {color} {(lambda count: "die" if count == 1 else "dice")(count)}', color)
    
    #  Literally roll the dice
    time.sleep(1) 
    print('\nYou rolled', end = '')
    for i in range(4):
        print('.', end = '')
        time.sleep(0.5)
    print(' ')
    for index, die in enumerate(current_dice):
        die.roll()
        if die._last_roll == 'shotgun':
            shotgun_count += 1
            background_color = 'on_red'
        elif die._last_roll == 'brains':
            brain_count += 1
            background_color = 'on_blue'
        else:
            background_color = None
        cprint(f'{ordinal(index + 1)} {die._color} die rolled ', end = '')
        cprint(f'{die._last_roll}', on_color = background_color)
        time.sleep(1)
    
    if shotgun_count >= 3:
        # Checks if you lost.
        cprint(f'\nYou\'ve been shot {shotgun_count} times. The round is over, and you scored 0 points.', 'magenta')
        print(' ')
        break

    # Update the player 
    cprint(f'\nYou\'ve eaten {brain_count} {(lambda n: "brain" if n == 1 else "brains")(brain_count)}.', 'green')
    cprint(f'You\'ve been shot {shotgun_count} {(lambda n: "time" if n == 1 else "times")(shotgun_count)}.', 'magenta')
    time.sleep(0.75)

    # Update the state
    current_dice = [die for die in current_dice if die._last_roll == 'footsteps']
    updated_dice_counter = Counter([die._color for die in current_dice])
    remaining_dice_counter = Counter([die._color for die in dice_list])


    # Tell the player what the remaining dice are
    if current_dice:
        print(f'\nIf you decide to roll again, you will be re-rolling: ')
        for color, count in updated_dice_counter.items():
            cprint(f'{count} {color} {(lambda n: "die" if n == 1 else "dice")(count)}', color)
    else:
        print('You will receive three new dice next round.')
    time.sleep(0.5)
    if len(current_dice) < 3:
        print(f'\nIf you roll again, you\'ll get {3 - len(current_dice)} new dice at random from the remaining dice:')
        for color, count in remaining_dice_counter.items():
            cprint(f'{count} {color} {(lambda count: "die" if count == 1 else "dice")(count)}', color)

    if len(dice_list) + len(current_dice) < 3:
        # You can only use 13 dice in total
        print('There are not enough dice left to continue playing')
        break

    # Ask the player if they're feeling lucky
    answer = ''
    print(' ')
    while answer not in ('y', 'yes', 'n', 'no'):
        answer = input('Would you like to keep keep rolling? (y/n): ')
        if answer in ('y', 'yes'):
            break
        if answer in ('no', 'n'):
            new_round = False
            break

# Report the results
if shotgun_count < 3:
    print('The round is over.')
    print(' ')
    time.sleep(0.5)
    cprint(f'You scored a total of {brain_count} points after {roll_number} {(lambda n: "rolls" if n > 1 else "roll")(roll_number)}.', 'cyan')
    time.sleep(0.5)
    cprint('You live to feed another day!', 'red')
    time.sleep(0.5)
    print(' ')

# This is an extraneous change I'm making to this file. 