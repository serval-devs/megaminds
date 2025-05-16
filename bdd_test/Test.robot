*** Settings ***
Resource    keywords.resource


*** Test Cases ***
#Do have the code double signs: ## . .
Verify of the code is correct
Verify that we get a error when the guess is too short
Verify that we get a error when the guess is too long
Verify that we get a error when the guess has the wrong signs


Check the result and the history after a guess
    Given The Game Is Started
    And The Game Is Started With Code #%#$
    When The Game Receives A New Guess #%%#
    Then Results should be ${result} #P=2, S=1
    And History should have guess #%%#

Is the attempt counter decreasing
    Given The Game Is Started
    And The Game Is Started With Code #%#$
    When The Game Receives 5 Guesses For #%#$
    Then The Number Of Guesses should be 5
    
Losing a Game
    Given The Game Is Started
    And The Game Is Started With Code ${code}
    When The Game Receives 10 Guesses for ${code}
    Then 
    
Winning a Game
Is it possible to start a new game after end game
