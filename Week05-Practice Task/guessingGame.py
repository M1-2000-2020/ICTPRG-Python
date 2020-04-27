import random
randomNumber = random.randint(0, 25)
guessCount = 0
correctGuess = False
totalCount = 7
items = []


while (guessCount <= 7 and correctGuess == False):
    guess = int(input("Enter a number inbetween 0 and 25: "))
    guessCount += 1
    items.append(guess)
    if (guess < randomNumber):
        print("Its too low, try again")
        print ("You have "+ str(totalCount - guessCount) + " guesses left")
    elif (guess > randomNumber):
        print("Its too high, try again")
        print ("You have "+ str(totalCount - guessCount) + " guesses left")
    else:
        print("You have guessed correctly !")
        correctGuess = True
        print(items)

        
