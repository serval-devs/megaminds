import os
from colorama import Fore, Style
from game import *

SEPARATOR_STRING = "------------------------"

RULES_STRING = """
You are playing the game MasterMind. 
The rules of MasterMind:
- A player only has 10 guesses.
- A code of length 4 has to be guessed.
- The valid symbols in the code are: ! @ # $ %
- Symbols can be present in the code multiple times.
- A player gets results after placing a guess
- The result consists of the amount of symbols that are on the correct place, which is presented with P[x]. And the correct amount of symbols that are present in the code, but not on the right place, which is presented with S[x].
- Previous guesses will be visible.
 
So, to win, a player must guess the code composed by the machine within 10 tries.
"""

GAME_WON_STRING = """
Congratulations!
Your guess {guess} was correct!
You have guessed it with {num_tries} tries.
 
Press ENTER to start a new game.
"""

GAME_LOST_STRING = """
GAME OVER!
You were not able to guess the correct code: {correct_code} within 10 tries.
 
Press ENTER to start a new game.
"""

clear = lambda: os.system('cls')

class UI:
    def __init__(self):
        self.game = Game()
        self.game.start("!!@#")

    def draw_instructions(self):
        print(SEPARATOR_STRING)
        print(RULES_STRING)
        print(SEPARATOR_STRING)

    def draw_board(self):
        board = self.game.get_board_entries()

        for i in range(MAX_TRIES):
            print(f"{i+1}) {board[i] if i < len(board) else ''}")

    def handle_guess(self):
        err = ""
        while True:
            print(Fore.RED + err + Style.RESET_ALL)
            guess = input("Your guess: ")
            match self.game.handle_turn(guess):
                case Msg.CodeHasInvalidSigns:
                    err = Msg.CodeHasInvalidSigns
                case Msg.CodeHasTooManySigns:
                    err = Msg.CodeHasTooManySigns
                case Msg.CodeHasNotEnoughSigns:
                    err = Msg.CodeHasNotEnoughSigns
                case Msg.ReachedMaxGuesses:
                    err = Msg.ReachedMaxGuesses
                case Msg.GameWon:
                    print(f"{Fore.GREEN}{Msg.GameWon}{Style.RESET_ALL}")
                    return
                case _:
                    return

    def restart(self):
        restart = input()
        if restart == "":
            self.game = Game()
            self.game.start("!!@#")

    def run_game_loop(self):
        while True:
            if ui.game._game_state == GameState.Running:
                clear()
                ui.draw_instructions()
                ui.draw_board()
                ui.handle_guess()
            elif ui.game._game_state == GameState.Lost:
                clear()
                ui.draw_instructions()
                ui.draw_board()
                correct_code = ui.game.get_code()
                print(GAME_LOST_STRING.format(correct_code=correct_code))
                self.restart()
            elif ui.game._game_state == GameState.Won:
                clear()
                ui.draw_instructions()
                ui.draw_board()
                correct_code = ui.game.get_code()
                num_tries = ui.game.get_guess_count()
                print(GAME_WON_STRING.format(guess=correct_code, num_tries=num_tries))
                self.restart()
            elif ui.game._game_state == GameState.NotRunning:
                break


ui = UI()
ui.run_game_loop()