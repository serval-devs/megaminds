from typing import List, Optional, Union, Tuple
from enum import StrEnum, Enum
from random import choices
from webbrowser import Error


class Msg(StrEnum):
    CodeHasNotEnoughSigns = "Not enough signs entered."
    CodeHasInvalidSigns = "Invalid signs entered."
    CodeHasTooManySigns = "Too many signs entered."
    InitialCodeInvalid = "Initial code is invalid."
    ReachedMaxGuesses = "The maximum number of guesses has been reached."
    GameWon = "You won the game!"
    GameNotRunning = "Game is not running!"

class GameState(Enum):
    NotRunning = 0
    Running = 1
    Lost = 2
    Won = 3

ACCEPTED_SYMBOLS = ["!", "@", "#", "$", "%"]
CODE_LENGTH = 4
MAX_TRIES = 10

def _count_correct_positions(code: str, guess: str) -> Tuple[int, List[str | None], List[str | None]]:
    result_pos = 0
    code_copy = list(code)
    guess_copy = list(guess)
    for i in range(len(code_copy)):
        if guess_copy[i] == code_copy[i]:
            result_pos += 1
            code_copy[i] = None
            guess_copy[i] = None
    return result_pos, code_copy, guess_copy


def _count_correct_symbols(code_list: List[str | None], guess_list: List[str | None]) -> int:
    result_sym = 0
    for i in range(len(guess_list)):
        if guess_list[i] is not None and guess_list[i] in code_list:
            result_sym += 1
            code_list[code_list.index(guess_list[i])] = None
    return result_sym


def _validate_code(input_str: str) -> Optional[Msg]:
    if len(input_str) < CODE_LENGTH:
        return Msg.CodeHasNotEnoughSigns
    elif len(input_str) > CODE_LENGTH:
        return Msg.CodeHasTooManySigns
    elif not all(s in ACCEPTED_SYMBOLS for s in input_str):
        return Msg.CodeHasInvalidSigns


class Game:
    def __init__(self, code_string: str= None):
        self.nr_of_guesses_left: int = MAX_TRIES
        self._game_state: GameState = GameState.NotRunning
        self._board: List[str] = []
        self._guesses: List[str] = []
        self._results: List[str] = []
        self._secret_code: str = ""
        self.last_result: str = ""

    def start(self, code_string: str = None) -> Optional[Msg]:
        if code_string is None:
            self._secret_code = "".join(choices(ACCEPTED_SYMBOLS, k=CODE_LENGTH))
            self._game_state = GameState.Running
        elif _validate_code(code_string) is None:
            self._secret_code = code_string
            self._game_state = GameState.Running
        else:
            return Msg.InitialCodeInvalid

    def _make_guess(self, guess: str) -> Optional[Msg]:
        if err := _validate_code(guess):
            return err

        pos_count, remaining_code, remaining_guess = _count_correct_positions(self._secret_code, guess)
        sym_count = _count_correct_symbols(remaining_code, remaining_guess)

        self._guesses.append(guess)
        self._results.append(result := f"P{pos_count}, S{sym_count}")
        self.last_result = result
        self._board.append(f"{guess} | {result}")

    def handle_turn(self, guess: str) -> Optional[Msg]:
        if self._game_state != GameState.Running:
            return Msg.GameNotRunning

        if self.nr_of_guesses_left > 0:
            if err := self._make_guess(guess):
                return err
            self.nr_of_guesses_left -= 1
            if guess == self._secret_code:
                self._game_state = GameState.Won
                return Msg.GameWon
            if self.nr_of_guesses_left == 0:
                self._game_state = GameState.Lost
        else:
            return Msg.GameNotRunning

    def get_board_entries(self) -> List[str]:
        return self._board

    def is_running(self) -> bool:
        return self._game_state == GameState.Running

    def get_code(self) -> Optional[str]:
        if self._game_state == GameState.Lost or self._game_state == GameState.Won:
            return self._secret_code

    def get_guess_count(self) -> int:
        return MAX_TRIES - self.nr_of_guesses_left

    def get_guesses(self) -> List[str]:
        return self._guesses

    def get_results(self) -> List[str]:
        return self._results