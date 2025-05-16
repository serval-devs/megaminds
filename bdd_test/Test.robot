*** Settings ***
Resource    keywords.resource


*** Test Cases ***
#Do have the code double signs: ## . .
Verify of the code is correct
Verify that we get a error when the guess is too short
Verify that we get a error when the guess is too long
Verify that we get a error when the guess has the wrong signs
Check the result after a guess
Is the attempt counter decreasing
Are the previous guesses in the history
Can the game end
Can we win the game
Is it possible to start a new game after end game