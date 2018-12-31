import time
import random

def main():
    """
    A simple number guessing game framework.
    """
    lowerLimit = 1
    upperLimit = 20
    correctGuess = random.randint(lowerLimit, upperLimit)
    currentGuess = 'wrong-number'
    maxTries = 5
    currentTry = 0
    pauseTime = 1

    print('I am thinking of a number between',lowerLimit,'and',upperLimit)
    print('You have',maxTries,'attempts to guess my number.')

    #
    # While we are not out of guesses and the correct number
    # hasn't been guessed, keep looping.
    #
    while (currentTry < maxTries) and (currentGuess != correctGuess):
        currentGuess = input('Guess my number: ')
        #
        # Make sure the user guesses a number.
        #
        while currentGuess.isdigit() == False:
            currentGuess = input('You have to guess a number: ')
        currentTry = currentTry + 1
        currentGuess = int(currentGuess)
        time.sleep(pauseTime)
        if currentGuess < correctGuess:
            print('My number is higher.')
        if currentGuess > correctGuess:
            print('My number is lower.')
            
    if currentGuess == correctGuess:
        print('Nice work! You guessed my number in ',currentTry,'tries.')
    else:
        print('You ran out of tires. My number was',correctGuess)

main()
