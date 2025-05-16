from typing import List

class Game:
    def __init__(self):
        self.nr_of_guesses: int = 0
        self.game_over: bool = False
        self.board = None

    def start(self):
        pass

    def handle_turn(self):
        return None

    def get_board(self):
        return None