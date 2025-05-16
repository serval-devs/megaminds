*** Settings ***
Library    game_test_api.py

*** Keywords ***
Starting the game
    The Game Is Started With Code #$@!

   
    

Results should be ${result}

The Game Receives ${amount} Guesses for ${code}

The Number Of Guesses should be ${amount}

History should have guess ${input}

