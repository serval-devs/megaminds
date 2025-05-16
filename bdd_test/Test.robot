*** Settings ***
Resource    keywords.resource

*** Test Cases ***
Verify of the code can have double signs
    Given The Game Is Started
    And The Game Is Started With Code ${code}
    When No Operation
    Then Verify that the code is accepted

Verify that we get a error when the guess is too short
    Given The Game Is Started
    And The Game Is Started With Code ${code}
    When The Game Receives A New Guess ${input}    #what is wrong
    Then The Game reports error ${error report}

Verify that we get a error when the guess is too long
    Given The Game Is Started
    And The Game Is Started With Code ${code}
    When The Game Receives A New Guess ${input}    #what is wrong
    Then The Game reports error ${error report}

Verify that we get a error when the guess has the wrong signs
    Given The Game Is Started
    And The Game Is Started With Code ${code}
    When The Game Receives A New Guess ${input}    #what is wrong
    Then The Game reports error ${error report}

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
