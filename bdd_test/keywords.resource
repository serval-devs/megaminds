*** Settings ***
Library    game_test_api.py

*** Keywords ***
The Game Is Started With Code ${code}

No Operation

Verify that the code is accepted

The Game reports error ${error report}



Results should be ${result}

The Game Receives ${amount} Guesses for ${code}

The Number Of Guesses should be ${amount}

History should have guess ${input}

