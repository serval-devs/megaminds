*** Settings ***
Resource    keywords.resource

*** Test Cases ***
Start a new game and verify of a code is generated
    Given The Game Is Started With Code #$!@
    When The Game Is Running
    Then Check If The Secret Is Equal To #$!@

Verify that we get a error when the guess is too short
    Given The Game Is Started
    And The Game Is Started With Code #$!@
    When The Game Receives A New Guess #$!    #what is wrong
    Then The Game reports error ${error report}


Verify that we get a error when the guess is too long
    Given The Game Is Started
    And The Game Is Started With Code #$!@
    When The Game Receives A New Guess #$!!$#    #what is wrong
    Then The Game reports error ${error report}

Verify that we get a error when the guess has the wrong signs
    Given The Game Is Started With Code #$!@
    When The Game Receives A New Guess #&*!    #what is wrong
    Then The Game reports error ${error report}

Check the result and the history after a guess
    Given The Game Is Started With Code #%#$
    When The Game Receives A New Guess #%%#
    Then History Should Have Guess #%%# | P2, S1

Is the attempt counter decreasing
    Given The Game Is Started With Code #%#$
    When The Game Receives A New Guess #%%#
    Then The Number Of Guesses should be 9

Losing a Game
    Given The Game Is Started With Code #%#$
    When The Game Receives 11 Guesses for #%#$
    Then The Game Should Show Lose message
    
Winning a Game
    Given The Game Is Started With Code #%%#
    When The Game Receives A New Guess #%%#
    Then The Game Should Show Winner message

