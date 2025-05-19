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
    And The Game Receives The Input !
    Then The Game Gives An Error When The Guess Is Too Short

Verify that we get a error when the guess is too long
    Given The Game Is Started
    And The Game Is Started With Code #$!@
    And The Game Receives The Input !!!!!
    Then The Game Gives An Error When The Guess Is Too Long

Verify that we get a error when the guess has the wrong signs
    Given The Game Is Started
    And The Game Is Started With Code #$!@
    And The Game Receives The Input abcd
    Then The Game Gives An Error When The Guess Contains Wrong Signs

Check the result and the history after a guess
    Given The Game Is Started
    And The Game Is Started With Code #%#$
    When The Game Receives A New Guess #%%#
    Then Results should be #%%#
    And History Should Have Guess #%%#
    And History Should Have Result #%%#

Is the attempt counter decreasing
    Given The Game Is Started
    And The Game Is Started With Code #%#$
    When The Game Receives 5 Guesses For #%#$
    Then The Number Of Guesses should be 5

Losing a Game
    Given The Game Is Started
    And The Game Is Started With Code #%#$
    When The Game Receives 10 Guesses for #%#$
    Then The Game Should Show Lose message
    
Winning a Game
    Given The Game Is Started
    And The Game Is Started With Code #%%#
    When The Game Receives A New Guess #%%#
    Then The Game Should Show Winner message

