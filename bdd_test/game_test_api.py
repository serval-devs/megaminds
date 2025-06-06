from game.game import Game, _validate_code
from robot.api.deco import keyword

class GameKeywords:
    def __init__(self):
        self.game = Game()

    @keyword("The Game Is Started")
    def start_game(self):
        if self.game.is_running():
            return
        self.game.start()

    @keyword("The Game Is Started With Code ${code}",
        types={'code': str})
    def start_game_with_code(self, code: str):
        if self.game.is_running():
            return
        return self.game.start(code)

    @keyword("The Game Receives A New Guess ${input}",
        types={'input': str})
    def handle_turn(self, input: str):
        return self.game.handle_turn(input)

    @keyword("Get The Game History")
    def get_board_entries(self):
        return self.game.get_board_entries()

    @keyword("The Game Is Running")
    def is_running(self):
        return self.game.is_running()

    @keyword("Get The Number Of Guesses")
    def get_guess_count(self):
        return self.game.get_guess_count()

    @keyword("Get All The Guesses")
    def get_guesses(self):
        return self.game.get_guesses()

    @keyword("Get All The Results")
    def get_results(self):
        return self.game.get_results()

    @keyword ("Get the secret code")
    def get_code(self):
        return self.game._secret_code

    @keyword("Get an invalid message ${input}",
             types={'input': str})
    def get_message(self):
        return _validate_code(input)
