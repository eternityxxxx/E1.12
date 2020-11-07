import hangman
import pytest


def test_loading_screen_success():
    data = [
        ' __    __       ___      .__   __.   _______ .___  ___.      ___      .__   __.',
        '|  |  |  |     /   \     |  \ |  |  /  _____||   \/   |     /   \     |  \ |  |',
        '|  |__|  |    /  ^  \    |   \|  | |  |  __  |  \  /  |    /  ^  \    |   \|  |',
        '|   __   |   /  /_\  \   |  . `  | |  | |_ | |  |\/|  |   /  /_\  \   |  . `  |',
        '|  |  |  |  /  _____  \  |  |\   | |  |__| | |  |  |  |  /  _____  \  |  |\   |',
        '|__|  |__| /__/     \__\ |__| \__|  \______| |__|  |__| /__/     \__\ |__| \__|',
    ]

    assert hangman.loading_interface(data) is None


def test_loading_screen_fail():
    data = []
    with pytest.raises(Exception):
        assert hangman.loading_interface(data)


@pytest.mark.parametrize('data,excepted', [('Joe', True), ('beast', True), (1, False), ('', False), ('U', False)])
def test_check_user_name(data, excepted):
    assert hangman.check_user_name(data) == excepted


@pytest.mark.skip(
    'Данный тест требует ввода данных с консоли, для тестирования уберите данный декоратор и используйте флаг -s с\
командой pytest'
)
def test_main_menu_interface_success():
    data = [
        '#######################################################',
        '#                                                     #',
        '#                     MAIN MENU:                      #',
        '#    1.) START THE GAME;                              #',
        '#    2.) VIEW THE LEADERBOARD (coming soon..);        #',
        '#    or press any key to leave..                      #',
        '#                                                     #',
        '#######################################################',
    ]
    user_name = 'Joe'

    assert hangman.main_menu_interface(data, user_name) is not None


def test_main_menu_interface_fail():
    data = []
    user_name = 'Joe'

    with pytest.raises(Exception):
        assert hangman.main_menu_interface(data, user_name)


@pytest.mark.skip(
    'Данный тест требует ввода данных с консоли, для тестирования уберите данный декоратор и используйте флаг -s с\
командой pytest'
)
def test_main_menu_choise():
    user_name = 'Joe'
    assert hangman.main_menu_choise(user_name) is not None


@pytest.mark.parametrize('data', [['SKILLFACTORY', 'UNITTEST'], ['PYTEST', 'coverage', 'blackbox']])
def test_word_choise_success(data):
    assert hangman.word_choise(data) is not None


def test_word_choise_fail():
    data = []
    with pytest.raises(Exception):
        assert hangman.word_choise(data)


def test_starting_interface():
    assert hangman.starting_game_interface() is None


@pytest.mark.parametrize('word,missed,hitted,attempts', [
    ('SKILLFACTORY', ['U', 'P'], ['S', 'Y', 'F'], 6),
    ('UNITTEST', ['P'], [], 1),
    ('BLACKBOX', [], ['B', 'A', 'C', 'K'], 4)
])
def test_view_game_status_success(word, missed, hitted, attempts):
    assert hangman.view_game_status(word, missed, hitted, attempts) is None


def test_view_game_status_fail():
    with pytest.raises(Exception):
        assert hangman.view_game_status('', [], [], 1)


@pytest.mark.skip(
    'Данный тест требует ввода данных с консоли, для тестирования уберите данный декоратор и используйте флаг -s с\
командой pytest'
)
@pytest.mark.parametrize('word,missed,hitted,attempts', [
    ('SKILLFACTORY', ['U', 'P'], ['S', 'Y', 'F'], 6),
    ('UNITTEST', ['P'], [], 1),
    ('BLACKBOX', [], ['B', 'A', 'C', 'K'], 4)
])
def test_player_guess(word, missed, hitted, attempts):
    assert hangman.player_guess(word, missed, hitted, attempts) is not None


@pytest.mark.skip(reason='Coming soon..')
def test_view_leaderboard():
    assert True
