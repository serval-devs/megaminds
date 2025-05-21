*** Settings ***
Resource    keywords.resource

*** Test Cases ***
Start a new game and verify of a code is generated with a sign multiple times in the code
    Given The Game Is Started With Code #!!@
    When The Game Is Running
    Then Check If The Secret Is Equal To #!!@

Verify that we get a error when the guess is too short
    Given The Game Is Started
    And The Game Receives The Input !
    Then The Game Gives An Error When The Guess Is Too Short
    And The Number Of Guesses should be 0
    And History Should Not Have Guess !

Verify that we get a error when the guess is too long
    Given The Game Is Started
    And The Game Receives The Input !!!!!
    Then The Game Gives An Error When The Guess Is Too Long
    And The Number Of Guesses should be 0
    And History Should Not Have Guess !!!!!

Verify that we get a error when the guess has the wrong signs
    Given The Game Is Started
    And The Game Receives The Input abcd
    Then The Game Gives An Error When The Guess Contains Wrong Signs
    And The Number Of Guesses should be 0
    And History Should Not Have Guess abcd

Check the result and the history after a guess
    Given The Game Is Started With Code #%#$
    When The Game Receives A New Guess #%%#
    Then History Should Have Guess #%%# | P2, S1

Is the attempt counter decreasing by 1
    Given The Game Is Started With Code #%#$
    When The Game Receives A New Guess #%%#
    Then The Number Of Guesses should be 1

Is the attempt counter decreasing by 5
    Given The Game Is Started With Code #%#$
    When The Game Receives 5 Guesses for #%#$
    Then The Number Of Guesses should be 5

There should only be 10 attempts
    Given The Game Is Started With Code #%#$
    When The Game Receives 11 Guesses for #%#$
    Then The Number Of Guesses should be 10
    And History Should Match Guesses
    And The Game Is Not Running
    And The Game Should Show An Error Message

Losing a Game
    Given The Game Is Started With Code #%#$
    When The Game Receives 10 Guesses for #%#$
    Then The Game Should Show Lose message

Winning a Game
    Given The Game Is Started With Code #%%#
    When The Game Receives The Input #%%#
    Then The Game Should Show Winner message

