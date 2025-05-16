# from game_objects import *
from typing import List, Optional, Union
from enum import StrEnum
from random import choices
from webbrowser import Error


class ErrorMsg(StrEnum):
    CodeHasNotEnoughSigns = "Not enough signs entered."
    CodeHasInvalidSigns = "Invalid signs entered."
    CodeHasTooManySigns = "Too many signs entered."
    InitialCodeInvalid = "Initial code is invalid."

ACCEPTED_SYMBOLS = ["!", "@", "#", "$", "%"]
CODE_LENGTH = 4
MAX_TRIES = 10

class Game:
    def __init__(self, code_string: str= None):
        self.nr_of_guesses_left: int = 0
        self.game_over: bool = False
        self.board: List[str] = None
        self.secret_code: List[str] = None

    def _validate_code(self, input_str: str) -> Union[ErrorMsg | None]:
        if len(input_str) < CODE_LENGTH:
            return ErrorMsg.CodeHasNotEnoughSigns
        elif len(input_str) > CODE_LENGTH:
            return ErrorMsg.CodeHasTooManySigns
        elif not all(s in ACCEPTED_SYMBOLS for s in input_str):
            return ErrorMsg.CodeHasInvalidSigns

    def start(self, code_string: str = None) -> Optional[ErrorMsg]:
        if code_string is None:
            self.secret_code = choices(ACCEPTED_SYMBOLS, k=CODE_LENGTH)
        elif self._validate_code(code_string) is None:
                self.secret_code = [char for char in code_string]
        else:
            return ErrorMsg.InitialCodeInvalid

    def handle_turn(self, input_str: str) -> Union[str | ErrorMsg]:
        validation = self._validate_code(input_str)
        # Return error message
        if validation is not None:
            return validation

        result_pos = 0
        result_sym = 0
        # Compare given input with the secret code
        input_str_list = [char for char in input_str]
        correct_code = self.secret_code

        for i, (guessed_char, true_char) in enumerate(zip(input_str_list, correct_code)):
            if guessed_char == true_char:
                # correct position and correct symbol
                result_pos += 1
                correct_code[i] = "x"
                input_str_list[i] = "x"

        for i, guessed_char in enumerate(input_str_list):
            for j, correct_char in enumerate(correct_code):
                if i is j:
                    continue

                if guessed_char is correct_char:
                    # correct symbol, incorrect pos
                    correct_code[j] = "x"
                    result_sym += 1
                    break

        return f"{input_str} | P{result_pos}, S{result_sym}"

    def get_board_entries(self) -> List[str]:
        return [""]

    def is_running(self) -> bool:
        return False

    def get_guess_count(self) -> int:
        return self.nr_of_guesses_left

    def get_guesses(self) -> List[str]:
        return self.board.get_guesses()

    def get_results(self) -> List[str]:
        return self.board.get_results()