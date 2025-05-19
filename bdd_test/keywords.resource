*** Settings ***
Library    game_test_api.py

*** Keywords ***
The Game Is Started With Code ${code}

No Operation

Verify that the code is accepted

The Game reports error ${error report}



The Number Of Guesses should be ${amount}
    ${guesses}=    Get Count
    Should Be Equal    ${guesses}    ${amount}

Results should be ${result}
    ${results}=    Get All The Results
    Should Contain    ${results}    ${result}

#als tijd over, meerdere guesses in history checken
History should have guess ${input}
    ${history}=    Get The Game History
    Should Contain    ${history}    ${input}

History Should Have Result ${result}
    ${history}=    Get The Game History
    Should Contain    ${history}    ${result}

The Game Receives ${amount} Guesses for ${code}


# winner messages includes: amount of guesses, correct code
The Game Should Show Lose message

# winner messages includes: amount of guesses, correct code
The Game Should Show Winner message