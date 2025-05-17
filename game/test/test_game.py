from webbrowser import Error

import pytest
from game.game import Game, _validate_code
from game.game import ErrorMsg

@pytest.fixture
def game():
    return Game()

def test_start_game_with_random_code():
    for i in range(100):
        game = Game()
        assert game.start() is None
        assert _validate_code("".join(game._secret_code)) is None

def test_start_game_with_input(game):
    assert game.start("aaaaa") == ErrorMsg.InitialCodeInvalid
    assert game.start("!$$#") is None

def test_is_running(game):
    game.start()
    assert game.is_running()

def test_is_code_valid(game):
    assert _validate_code("aaaa") == ErrorMsg.CodeHasInvalidSigns
    assert _validate_code("#####") == ErrorMsg.CodeHasTooManySigns
    assert _validate_code("###") == ErrorMsg.CodeHasNotEnoughSigns
    assert _validate_code("!@@a") == ErrorMsg.CodeHasInvalidSigns
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
    ("!@#$", "!@#$", "P4, S0"),
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
    ("@@##", "@#!@#", ErrorMsg.CodeHasTooManySigns),
    ("@@##", "@#!", ErrorMsg.CodeHasNotEnoughSigns),
    ("@@##", "@#!a", ErrorMsg.CodeHasInvalidSigns),
])
def test_handle_invalid_turn(game, code, guess, expected_error_msg):
    game.start(code)
    assert game.handle_turn(guess) == expected_error_msg

# def test_board(game):
#     game.start("!@#$")
#     assert game.handle_turn("!%%%") is None
#     assert game.handle_turn("!%%$") is None
#     assert game.handle_turn("!@#%") is None
#     assert game.handle_turn("!@#$") is None
#     print(game._board)