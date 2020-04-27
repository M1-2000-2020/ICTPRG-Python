import random
randomNumber = random.randint(1,6)
diceCount = 0
correctGuess = False
sumAttempts = 7
items = []


while (diceCount <= 5) and (correctGuess == False):
    diceCount += 1
    items.append(randomNumber)
print(items)