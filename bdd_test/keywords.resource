*** Settings ***
Library    megaminds.bdd_test.game_test_api.GameKeywords

*** Keywords ***
Start a new board game
    The Game Is Started
    ${isRunning}=    The Game Is Running
    Should Be True    ${isRunning}

Check if the secret is equal to ${myCode}
    ${locCode}=    Get The Secret Code
    Should Be Equal    ${locCode}    ${myCode}

The Number Of Guesses should be ${amount}
    ${guesses}=    Get The Number Of Guesses
    ${amount}=    Convert To Integer    ${amount}
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

The Game Receives ${amount} Guesses for ${code}
    FOR    ${index}    IN RANGE    ${amount}
        ${input}=    Generate Valid Input    ${code}
        The Game Receives A New Guess ${input}
    END

Generate Valid Input
    [Arguments]    ${code}
    ${input}=    Generate Random Input
    WHILE    '${input}' == '${code}'
        ${input}=    Generate Random Input
    END
    [Return]    ${input}

Generate Random Input
    ${input}=    Evaluate    ''.join(random.choices(['!', '$', '#', '%', '&'], k=4))    modules=random
    [Return]    ${input}

