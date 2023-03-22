import Live as Game
import random
import time


def play(game_difficulty):
    sequence_number = generate_sequence(game_difficulty)
    display_text_for_user(sequence_number)
    user_number = get_list_from_user(game_difficulty)

    if is_list_equal(user_number, sequence_number):
        time.sleep(2)
        Game.player_finished()
    else:
        print('You lost !! Better luck next time!')
        print('The numbers that were generated are:', *sequence_number)
        time.sleep(2)
        Game.player_finished()


def generate_sequence(game_difficulty):
    generate = [random.randint(1, 101) for i in range(game_difficulty)]
    return generate


def is_list_equal(list1, list2):
    if list1 != list2:
        return False
    else:
        return True


def get_list_from_user(game_difficulty):
    user_list = [get_valid_sequence() for i in range(game_difficulty)]
    return user_list


def get_valid_sequence():
    while True:
        user_number = input('Enter a number from the sequence: ')
        if len(user_number) == 1 or len(user_number) == 2:
            # and user_number in '12345678910':
            return int(user_number)
        else:
            print('Invalid input, Please enter a number between 1 and 10 each time.')


def display_text_for_user(sequence_numbers):

    print('\nYou will need to input the numbers same as the list that will be shown in a moment.')
    time.sleep(2)

    print('\nBe ready and remember the numbers...')
    time.sleep(2)

    print(*sequence_numbers)
    time.sleep(0.7)

    Game.clear_screen()
    print('\nNow try to repeat it!\n')
