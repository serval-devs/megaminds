*** Settings ***
Resource    keywords
Library    game_test_api.py

*** Test Cases ***
Verify of the code can have double signs
    Given Start a game with this code ${code}
    When No Operation
    Then Verify that the code is accepted

Verify that we get a error when the guess is too short
    Given Start a game with this code ${code}
    When The Game Receives A New Guess {input}    #what is wrong
    Then The Game reports error

Verify that we get a error when the guess is too long
    Given Start a game with this code ${code}
    When The Game Receives A New Guess {input}    #what is wrong
    Then The Game reports error
    
Verify that we get a error when the guess has the wrong signs
    Given Start a game with this code ${code}
    When The Game Receives A New Guess {input}    #what is wrong
    Then The Game reports error ${error report}
    
Check the result after a guess

Is the attempt counter decreasing
Are the previous guesses in the history
Can the game end
Can we win the game
Is it possible to start a new game after end game