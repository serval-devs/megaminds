from webbrowser import Error

import pytest
from game.game import Game, _validate_code, MAX_TRIES
from game.game import Msg

@pytest.fixture
def game():
    return Game()

@pytest.fixture
def won_game():
    game = Game()
    game.start("!!!!")
    game.handle_turn("!!!!")
    return game

@pytest.fixture
def lost_game():
    game = Game()
    game.start("!!!!")
    for i in range(MAX_TRIES):
        game.handle_turn("@@@@")
    return game

def test_start_game_with_random_code():
    for i in range(100):
        game = Game()
        assert game.start() is None
        assert _validate_code("".join(game._secret_code)) is None

def test_start_game_with_input(game):
    assert game.start("aaaaa") == Msg.InitialCodeInvalid
    assert game.start("!$$#") is None

def test_is_running(game):
    game.start()
    assert game.is_running()

def test_is_code_valid(game):
    assert _validate_code("aaaa") == Msg.CodeHasInvalidSigns
    assert _validate_code("#####") == Msg.CodeHasTooManySigns
    assert _validate_code("###") == Msg.CodeHasNotEnoughSigns
    assert _validate_code("!@@a") == Msg.CodeHasInvalidSigns
    assert _validate_code("!@#$") is None
    assert _validate_code("!!@@") is None

@pytest.mark.parametrize("code, guess, expected_result",[
    ("@@##", "!!@!", "P0, S1"),
    ("@@##", "!!!@", "P0, S1"),
    ("@@##", "!!@@", "P0, S2"),
    ("!@#$", "$#@%", "P0, S3"),
    ("!@#$", "$#@!", "P0, S4"),
])
def test_handle_valid_turn_symbols(game, code, guess, expected_result):
    game.start(code)
    assert game.handle_turn(guess) is None
    assert game.last_result == expected_result

@pytest.mark.parametrize("code, guess, expected_result",[
    ("!!@#", "$$$!", "P0, S1"),
    ("!!@#", "$$!!", "P0, S2"),
    ("!!!#", "$$$!", "P0, S1"),
])
def test_handle_valid_turn_correct_symbols_with_duplicate_symbols(game, code, guess, expected_result):
    game.start(code)
    assert game.handle_turn(guess) is None
    assert game.last_result == expected_result

@pytest.mark.parametrize("code, guess, expected_result",[
    ("!@#$", "!%%%", "P1, S0"),
    ("!@#$", "!%%$", "P2, S0"),
    ("!@#$", "!@#%", "P3, S0"),
])
def test_handle_valid_turn_positions_and_symbols(game, code, guess, expected_result):
    game.start(code)
    assert game.handle_turn(guess) is None
    assert game.last_result == expected_result

@pytest.mark.parametrize("code, guess, expected_result",[
    ("!!@@", "!!!%", "P2, S0"),
    ("!@@!", "!%!!", "P2, S0"),
])
def test_handle_valid_turn_positions_and_symbols_with_duplicate_symbols(game, code, guess, expected_result):
    game.start(code)
    assert game.handle_turn(guess) is None
    assert game.last_result == expected_result

@pytest.mark.parametrize("code, guess, expected_result",[
    ("@@##", "@#$$", "P1, S1"),
    ("@@%$", "@@$%", "P2, S2"),
])
def test_handle_valid_turn_both_p_and_s_non_zero(game, code, guess, expected_result):
    game.start(code)
    assert game.handle_turn(guess) is None
    assert game.last_result == expected_result

@pytest.mark.parametrize("code, guess, expected_error_msg",[
    ("@@##", "@#!@#", Msg.CodeHasTooManySigns),
    ("@@##", "@#!", Msg.CodeHasNotEnoughSigns),
    ("@@##", "@#!a", Msg.CodeHasInvalidSigns),
])
def test_handle_invalid_turn(game, code, guess, expected_error_msg):
    game.start(code)
    assert game.handle_turn(guess) == expected_error_msg

def test_winning_first_try(game):
    code = "@!$#"
    game.start(code)
    assert game.handle_turn("@!$#") == Msg.GameWon

def test_winning_last_try(game):
    code = "@!$#"
    game.start(code)

    for i in range(MAX_TRIES-1):
        assert game.handle_turn("@@@@") is None and game.nr_of_guesses_left == MAX_TRIES-i-1
    assert game.handle_turn("@!$#") == Msg.GameWon

def test_cannot_win_after_max_tries(game):
    code = "@!$#"
    game.start(code)

    for i in range(MAX_TRIES):
        assert game.handle_turn("@@@@") is None and game.nr_of_guesses_left == MAX_TRIES-i-1
    assert game.handle_turn("@!$#") is Msg.GameNotRunning and game.nr_of_guesses_left == 0

def test_winning_seventh_try(game):
    code = "@!$#"
    game.start(code)

    for i in range(6):
        assert game.handle_turn("@@@@") is None and game.nr_of_guesses_left == MAX_TRIES-i-1
    assert game.handle_turn("@!$#") == Msg.GameWon and game.nr_of_guesses_left == 3

def test_won_game(won_game):
    assert won_game.handle_turn("@!$#") == Msg.GameNotRunning

@pytest.mark.parametrize("input_str",["!!!!", "!!!", "!!!!!", "a!!!"])
def test_game_not_running(game, input_str):
    assert game.handle_turn(input_str) == Msg.GameNotRunning

def test_get_board(game):
    game.start("!!@#")
    assert game.handle_turn("!#%%") is None
    assert game.get_board_entries() == ["!#%% | P1, S1"]
    assert game.handle_turn("!!##") is None
    assert game.get_board_entries() == ["!#%% | P1, S1", "!!## | P3, S0"]
    assert game.handle_turn("!!@#") is Msg.GameWon
    assert game.get_board_entries() == ["!#%% | P1, S1", "!!## | P3, S0", "!!@# | P4, S0"]
    assert game.handle_turn("!!@#") is Msg.GameNotRunning
    # assert game.get_board_entries() == ["!#%% | P1, S1", "!!## | P3, S0", "!!@# | P4, S0", "!!@# | P4, S0"]
    print(game.get_board_entries())
# def test_board(game):
#     game.start("!@#$")
#     assert game.handle_turn("!%%%") is None
#     assert game.handle_turn("!%%$") is None
#     assert game.handle_turn("!@#%") is None
#     assert game.handle_turn("!@#$") is None
#     print(game._board)