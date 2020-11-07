import os
import random
import time

LOADING_SCREEN = [
    ' __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.',
    '|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |',
    '|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |',
    '|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |',
    '|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |',
    '|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|',
]

GAMEEND_SCREENS = [
'''
        +---+
        |   |
            |
            |
            |
            |
     =========
''',
'''

        +---+
        |   |
        O   |
            |
            |
            |
     =========
''',
'''
        +---+
        |   |
        O   |
        |   |
            |
            |
     =========
''',
'''
        +---+
        |   |
        O   |
       /|   |
            |
            |
     =========
''',
'''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
     =========
''',
'''

        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
     =========
''',
'''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
     =========
''',
]

MAIN_MENU = [
    '#######################################################',
    '#                                                     #',
    '#                     MAIN MENU:                      #',
    '#    1.) START THE GAME;                              #',
    '#    2.) VIEW THE LEADERBOARD (coming soon..);        #',
    '#    or press any key to leave..                      #',
    '#                                                     #',
    '#######################################################',
]

WORDS = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']


def loading_interface(loading_screen):
    os.system('cls')
    if loading_screen:
        for line in loading_screen:
            print(line)
            time.sleep(1)
        return
    raise Exception('THE LOADING SCREEN DAMAGED OR DESTROYED')


def main_menu_interface(main_menu, user_name):
    os.system('cls')
    if main_menu:
        for line in main_menu:
            print(line)
        player_choise = main_menu_choise(user_name)
        return player_choise
    raise Exception('THE MAIN MENU INTERFACE DAMAGED OR DESTROYED')


def starting_game_interface():
    os.system('cls')
    print('THE WORD IS HIDDEN!')
    for i in reversed(range(1, 4)):
        print('start in ' + str(i) + '..')
        time.sleep(1)


def get_user_name():
    while True:
        user_name = input('Hi! What\'s your name?\n').lower()
        check = check_user_name(user_name)
        if check:
            return user_name
        print('This name is not correct! Try again..')


def check_user_name(name):
    if str(name).isdigit():
        return False
    if name == '' or len(name) < 2:
        return False
    return True


def main_menu_choise(user_name):
    return input('Hey ' + str(user_name) + '!' + ' What do you want? Choose one of the action..\n').lower()


def game_win(word):
    os.system('cls')
    print('You win! Great job.. The word was ' + word)
    time.sleep(5)
    game()


def game_lose(word, lose_screen):
    os.system('cls')
    print('You lose :( The word was: ' + word)
    time.sleep(2)
    for screen in reversed(lose_screen):
        print(screen)
        time.sleep(1)
    game()


def player_guess(word, missed, hitted, attempts):
    while True:
        guess = input('Enter the letter:\n').upper()
        if len(guess) > 1 or guess.isdigit() or guess == '':
            print('It\'s not a letter! Try it again..')
            continue
        if guess in missed:
            print('This letter has already been, let\'s do it again!')
        elif guess in hitted:
            print('This letter has already been, let\'s do it again!')
        else:
            if guess in word:
                print('HIT! :)')
                time.sleep(2)
                hitted.append(guess)
                return missed, hitted, attempts
            else:
                print('MISS.. :(')
                time.sleep(2)
                missed.append(guess)
                return missed, hitted, attempts - 1


def view_word_state(word, hitted):
    word_state = ''
    for letter in word:
        if letter in hitted:
            word_state += letter
        else:
            word_state += '_'
    if '_' in word_state:
        return word_state
    else:
        return ''


def view_game_status(word, missed, hitted, attempts):
    os.system('cls')

    if word:
        guess_word = view_word_state(word, hitted)
        if '_' in guess_word:
            print('The word is:\n' + guess_word)
            time.sleep(1)
        else:
            game_win(word)
    else:
        raise Exception('THE WORDS FOR SEARCHING DAMAGED OR DESTROYED')

    if attempts > 0:
        print('Your attempts:\n' + str(attempts))
        time.sleep(1)

    if missed:
        print('Misses: \n' + '-'.join(missed))
        time.sleep(1)

    if hitted:
        print('Hits: \n' + '-'.join(hitted) + '\n')
        time.sleep(1)


def word_choise(words_list):
    return random.choice(words_list).upper()


def start_game():
    word_for_hitting = word_choise(WORDS)
    attempts_left = len(word_for_hitting) - 1
    missed_letters = []
    hitted_letters = []
    game_is_done = False

    starting_game_interface()

    while not game_is_done:
        if attempts_left > 0:
            view_game_status(word_for_hitting, missed_letters, hitted_letters, attempts_left)
            new_missed, new_hitted, new_attempts = player_guess(
                word_for_hitting,
                missed_letters,
                hitted_letters,
                attempts_left,
            )
            missed_letters = new_missed
            hitted_letters = new_hitted
            attempts_left = new_attempts
        else:
            game_lose(word_for_hitting, GAMEEND_SCREENS)
            game_is_done = True


def view_leaderboard():
    pass


def actions(choise):
    if choise == '1':
        start_game()
    if choise == '2':
        view_leaderboard()
    exit(0)


def game():
    loading_interface(LOADING_SCREEN)
    player_name = get_user_name()
    menu_choise = main_menu_interface(MAIN_MENU, player_name)
    actions(menu_choise)


if __name__ == '__main__':
    game()
