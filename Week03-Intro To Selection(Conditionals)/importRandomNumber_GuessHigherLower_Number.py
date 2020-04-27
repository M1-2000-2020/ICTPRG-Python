import random
randomNum = random.randint(0,20)
correctGuess = 0

while (correctGuess == 0):
    guess = int(input("Enter a number between 0 and 20: "))
    if (guess > 20):
        print("Unfortunately you can not enter a number above 20!")
    elif (guess < 0):
        print("Unfortunately you can not enter a number below 0!")
    elif guess < randomNum:
        print("You need to guess a higher number: ")
    elif guess > randomNum:
        print("You need to guess a lower number: ")
    else:
        print("You have the correct number. Congratulations! ")
        correctGuess = 1

