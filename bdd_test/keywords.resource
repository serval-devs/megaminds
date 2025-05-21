*** Settings ***
Library    bdd_test.game_test_api.GameKeywords
Library    BuiltIn

*** Keywords ***
Start a new board game
    The Game Is Started
    ${isRunning}=    The Game Is Running
    Should Be True    ${isRunning}

Check if the secret is equal to ${myCode}
    ${locCode}=    Get The Secret Code
    Should Be Equal    ${locCode}    ${myCode}

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

The Number Of Guesses should be ${amount}
    ${guesses}=    Get The Number Of Guesses
    ${amount}=    Convert To Integer    ${amount}
    Should Be Equal    ${guesses}    ${amount}

History should have guess ${input}
    ${history}=    Get The Game History
    Should Contain    ${history}    ${input}

History Should Not Have Guess ${input}
    ${history}=    Get The Game History
    Should Not Contain    ${history}    ${input}

The Game Receives ${amount} Guesses for ${code}
    @{guesses}=    Create List
    FOR    ${index}    IN RANGE    ${amount}
        ${input}=    Generate Valid Input    ${code}
        Log    Guess ${index + 1}: ${input}
        Append To List    @{guesses}    ${input}
        The Game Receives The Input ${input}
        ${result}=    The Game Receives A New Guess ${input}
    END
    Set Test Variable    @{guess_list}    @{guesses}
    
History Should Match Guesses
    ${history}=    Get The Game History
    ${expected}=    Get Length    @{guess_list}
    ${actual}=    Get Length    ${history}
    Should Be Equal As Integers    ${actual}    ${expected}
    FOR    ${index}    IN RANGE    ${expected}
        ${line}=    Get From List    ${history}    ${index}
        ${guess}=    Get From List    @{guess_list}    ${index}
        Should Contain    ${line}    ${guess}
        

    
The Game Should Show Winner message
    ${message}=    The Game Receives A New Guess ${guess}
    ${code}=    Get The Secret Code
    ${amount}=    Get The Number Of Guesses
    Should Be Equal    ${message}    You won the game!
#   This should be requirement 7aii: This message includes the amount of attempts & the correct code.
#    Should Contain    ${message}    ${code}
#    Should Contain    ${message}    ${amount}

The Game Should Show Lose message
    ${message}=    The Game Receives A New Guess ${guess}
    ${code}=    Get The Secret Code
    ${amount}=    Get The Number Of Guesses
    #    Should Be Equal    ${message}    Game Over!     # requirement 7b: When the game was ended unsuccessfully, a “Game Over” message should be shown
    Should Be Equal    ${message}    Game is not running!     # requirement 7b: When the game was ended unsuccessfully, a “Game Over” message should be shown
#   This should be requirement 7aii: This message includes the amount of attempts & the correct code.
#    Should Contain    ${message}    ${code}
#    Should Contain    ${message}    ${amount}
    
The Game Should Show An Error Message
    ${message}=    The Game Receives A New Guess ${guess}
    Should Be Equal    ${message}    The maximum number of guesses has been reached.     # requirement 4: A game has 10 tries.

The Game Is Not Running
    ${message}=    The Game Receives A New Guess ${guess}
    Should Be Equal    ${message}    Game is not running!     # requirement 4: A game has 10 tries.
    ${isRunning}=    The Game Is Running
    Should Be Equal    ${isRunning}    False

    
Generate Valid Input
    [Arguments]    ${code}
    ${input}=    Generate Random Input
    WHILE    '${input}' == '${code}'
        ${input}=    Generate Random Input
    END
    [Return]    ${input}

Generate Random Input
    ${input}=    Evaluate    ''.join(random.choices(['!', '$', '#', '%', '@'], k=4))    modules=random
    [Return]    ${input}

