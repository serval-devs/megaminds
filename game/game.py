from game_objects import *
from error_messages import *
from typing import List, Optional
from error_messages import ErrorMsg


class Game:
    def __init__(self, code_string: str= None):
        self.nr_of_guesses_left: int = 0
        self.game_over: bool = False
        self.board = Board()
        self.secret_code = Code(code_string)

    def start(self, code_string: str = None) -> Optional[ErrorMsg]:
        return None

    def handle_turn(self, input_str: str) -> Result:
        return None

    def get_board_entries(self) -> List[str]:
        return [""]

    def is_running(self) -> bool:
        return False

    def get_guess_count(self) -> int:
        return self.nr_of_guesses_left

    def get_guesses(self) -> List[Guess]:
        return self.board.get_guesses()

    def get_results(self) -> List[Result]:
        return self.board.get_results()