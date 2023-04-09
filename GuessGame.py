import os
import random, time
from GameDetails import game_details

def generate_number():
    generate = random.randint(1, int(game_details['game_difficulty']) * 20)
    return generate


def compare_results(guess):
    return guess


def get_guess_from_user(number):
    guess = None
    tries = 0

    while guess != number:
        guess = compare_results(input('Your guess: '))
        tries += 1
        if int(tries) == 4:
            print('Sorry, you ran out of tries')
            print('The number was ', int(number))
            time.sleep(2)
            os.system('cls')
            return False
        if guess.isdigit():
            if int(guess) < int(number):
                print('The number is higher.')
            elif int(guess) > int(number):
                print('The number is lower.')
            elif int(guess) == int(number):
                print('You got it in', tries, 'tries!')
                time.sleep(2)
                os.system('cls')
                return True
        else:
            print('Please enter a valid number')


def guess_play(difficulty):
    secret_number = generate_number()

    print('Im thinking of a number between 1 and ', int(difficulty * 20))
    time.sleep(1)
    print('You have 3 tries to guess the number')
    time.sleep(1)
    print('Do you think you can guess the number?')

    get_guess_from_user(secret_number)


