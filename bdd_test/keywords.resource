*** Settings ***
Library    bdd_test.game_test_api.GameKeywords

*** Keywords ***
Start a new board game
    The Game Is Started
    ${isRunning}=    The Game Is Running
    Should Be True    ${isRunning}

Check if the secret is equal to ${myCode}
    ${locCode}=    Get The Secret Code
    Should Be Equal    ${locCode}    ${myCode}

The Number Of Guesses should be ${amount}
    ${guesses}=    Get Count
    Should Be Equal    ${guesses}    ${amount}

Results should be ${result}
    ${results}=    Get All The Results
    Should Contain    ${results}    ${result}

History should have guess ${input}
    ${history}=    Get The Game History
    Should Contain    ${history}    ${input}

History Should Have Result ${result}
    ${history}=    Get The Game History
    Should Contain    ${history}    ${result}

The Game Receives The Input ${input}
    set test variable    $guess    ${input}

The Game Gives An Error When The Guess Is Too Short
    ${error}=    The Game Receives A New Guess ${guess}
    Should Be Equal    ${error}    Not enough signs entered.

The Game Gives An Error When The Guess Is Too Long
    ${error}=    The Game Receives A New Guess ${guess}
    Should Be Equal    ${error}    Too many signs entered.

The Game Gives An Error When The Guess Contains Wrong Signs
    ${error}=    The Game Receives A New Guess ${guess}
    Should Be Equal    ${error}    Invalid signs entered.
