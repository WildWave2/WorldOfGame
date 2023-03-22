from GuessGame import play as load_guess_game
from MemoryGame import play as load_memory_game
from CurrencyGame import play as load_currency_roulette

import os

game_details = {

}


# - - - - - - - - - - - - - - - - - - - - - - Main Functions - - - - - - - - - - - - - - - - - -

def main():
    player_name = valid_name()
    game_details['name'] = player_name
    welcome(player_name)


def welcome(name):
    print('Hello, ' + name + ' and welcome to the World of Games (WoG).')
    print('Here you can find many cool games to play versus the computer')
    print('There is different difficulty for each of these games by '
          'choosing 1 for the easiest and 5 for the most complicated ones')
    print('1 - Memory Game')
    print('2 - Guess Game')
    print('3 - Currency Roulette')
    game_id = input('Please choose your game by entering the number of the game you want to play: ')
    while not game_id.isnumeric() or int(game_id) > 3 or int(game_id) < 1:
        print('Please enter a valid number')
        game_id = input('Please choose your game by entering the number of the game you want to play: ')
    game_details['game_id'] = game_id
    select_difficulty(game_id)


def select_difficulty(game):
    game_names = ['Memory Game', 'Guess Game', 'Currency Roulette']
    game_difficulty = input('Please choose the difficulty of the game ' + game_names[int(game) - 1] + ': ')
    while not game_difficulty.isnumeric() or int(game_difficulty) > 5 or int(game_difficulty) < 1:
        print('Please enter a valid number')
        game_difficulty = input('Please choose the difficulty of the game ' + game_names[int(game) - 1] + ': ')
    game_details['game_difficulty'] = game_difficulty
    start_game(game, game_difficulty)


def start_game(game, difficulty):

    if game == 1: load_memory_game(difficulty)
    elif game == 2: load_guess_game(difficulty)
    else: load_currency_roulette(difficulty)


def valid_name():
    while True:
        player_name = input('Please enter your name: ')
        if len(player_name) <= 2 or len(player_name) >= 20 or not player_name.isalpha():
            print('Please enter a valid name')
        else:
            return player_name
# - - - - - - - - - - - - - - - - - - - FINISH GAME - - - - - - - - - - - - - - - - -


def player_finished():
    print('\nWhat do you want to do next?\n')
    print('1 - Play Again')
    print('2 - Back to the main menu')
    print('3 - Change the difficulty of the game')
    print('4 - Exit')
    answer = input('Please enter your choice: ')
    restart_game(answer, game_details['game_difficulty'])


def restart_game(answer, difficulty):
    if answer == '1':
        if game_details['game_id'] == '1':
            load_memory_game(difficulty)
        elif game_details['game_id'] == '2':
            load_guess_game(difficulty)
        elif game_details['game_id'] == '3':
            load_currency_roulette(difficulty)
    elif answer == '2':
        welcome(game_details['name'])
    elif answer == '3':
        select_difficulty(int(game_details['game_id']))
    else:
        exit()


def clear_screen():
    os.system('cls')
