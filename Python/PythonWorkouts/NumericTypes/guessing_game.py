#!/usr/bin/env python

"""
Number guessing Game
"""

import random

def guessing_game():
    """
    Generate a random number between 1 to 100, and ask for the input till 
    you guess the number
    """
    answer = random.randint(1,100)
    noOfGuess = random.randint(1,5)

    while noOfGuess:
        user_guess = int(input('Whats your guess? '))

        if user_guess == answer:
            print(f'Right! your guess is correct')
            break
        elif user_guess < answer:
            print(f'You guess is too low')
        else:
            print(f'You guess is too high')

        noOfGuess = noOfGuess - 1
    else:
        print(f'no of guess is over')
    
        
    
guessing_game()
        