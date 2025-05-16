import pytest
from game.game import Game
from game.game import ErrorMsg

# @pytest.fixture
# def game():
#     game = Game()
#     return game

def test_start_game_with_no_input():
    for i in range(100):
        game = Game()
        assert game.start() is None
        assert game._validate_code("".join(game.secret_code)) is None

def test_start_game_with_input():
    game = Game()
    assert game.start("aaaaa") == ErrorMsg.InitialCodeInvalid
    assert game.start("!$$#") is None

def test_is_running():
    game = Game()
    game.start()
    assert game.is_running()

def test_is_code_valid():
    game = Game()
    assert game._validate_code("aaaa") is not None
    assert game._validate_code("#####") is not None
    assert game._validate_code("###") is not None
    assert game._validate_code("!@@a") is not None
    assert game._validate_code("!@#$") is None
    assert game._validate_code("!!@@") is None

def test_handle_valid_turn_symbols():
    game = Game()
    code = "@@##"
    guess = "!!@!"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P0, S1"

    game = Game()
    code = "@@##"
    guess = "!!!@"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P0, S1"

    game = Game()
    code = "@@##"
    guess = "!!@@"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P0, S2"

    game = Game()
    code = "!@#$"
    guess = "$#@%"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P0, S3"

    game = Game()
    code = "!@#$"
    guess = "$#@!"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P0, S4"

def test_handle_valid_turn_correct_symbols_with_duplicate_symbols():
    game = Game()
    code = "!!@#"
    guess = "$$$!"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P0, S1"

    game = Game()
    code = "!!@#"
    guess = "$$!!"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P0, S2"

    game = Game()
    code = "!!!#"
    guess = "$$$!"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P0, S1"

def test_handle_valid_turn_positions_and_symbols():
    game = Game()
    code = "!@#$"
    guess = "!%%%"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P1, S0"

    game = Game()
    code = "!@#$"
    guess = "!%%$"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P2, S0"

    game = Game()
    code = "!@#$"
    guess = "!@#%"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P3, S0"

    game = Game()
    code = "!@#$"
    guess = "!@#$"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P4, S0"

def test_handle_valid_turn_positions_and_symbols_with_duplicate_symbols():
    game = Game()
    code = "!!@@"
    guess = "!!!%"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P2, S0"

    game = Game()
    code = "!@@!"
    guess = "!%!!"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P2, S0"

def test_handle_valid_turn_both_p_and_s_non_zero():
    game = Game()
    code = "@@##"
    guess = "@#$$"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P1, S1"

    game = Game()
    code = "@@%$"
    guess = "@@$%"
    game.start(code)
    out = game.handle_turn(guess)
    assert out == f"{guess} | P2, S2"

def test_handle_invalid_turn():
    game = Game()
    game.start("@@##")
    out = game.handle_turn("@#!@#")
    assert out == ErrorMsg.CodeHasTooManySigns

    game = Game()
    game.start("@@##")
    out = game.handle_turn("@#!")
    assert out == ErrorMsg.CodeHasNotEnoughSigns

    game = Game()
    game.start("@@##")
    out = game.handle_turn("@#!a")
    assert out == ErrorMsg.CodeHasInvalidSigns

