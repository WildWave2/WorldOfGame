import Live as Game
import random

from currency_converter import CurrencyConverter

MAX_RANGE = 10


def convert_usd_to_ils(usd_amount):
    usd_to_nis = CurrencyConverter().convert(usd_amount, "USD", "ILS")
    interval = usd_to_nis
    return interval


def difficulty_range(difficulty):
    return MAX_RANGE - (int(difficulty) - 1) * 2


def play(difficulty):
    usd_amount = random.randint(1, 100)
    ils_amount = convert_usd_to_ils(int(usd_amount))
    print(usd_amount)
    print(ils_amount)
    diff_range = difficulty_range(difficulty)
    print(usd_amount, ils_amount, diff_range)
    while True:
        user_guess = float(input('Guess the value of USD {:.2f} in ILS: '.format(usd_amount)))

        if abs(user_guess - ils_amount) <= diff_range:
            print('You are close enough! The actual value is ', format(ils_amount), ' ILS.')
            Game.player_finished()
            play_again = input('Do you want to play again? (y/n) ')
            if play_again.lower() == 'n':
                Game.player_finished()
                break
        else:
            if user_guess < ils_amount:
                print('Your guess is too low. Try again.')
            else:
                print('Your guess is too high. Try again.')
