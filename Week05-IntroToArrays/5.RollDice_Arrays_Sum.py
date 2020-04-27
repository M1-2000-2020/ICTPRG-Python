
import random

numOfRolls=int(input("How many times would you like to roll the dice? (number needs to be inbetween 1 - 4) : "))
totalCount = 1
countArray = []

while (totalCount <= numOfRolls):
    rolled = random.randint(1, 6)
    print("The dice rolled and you have thrown the number: ", rolled)
    totalCount += 1
    countArray.append(rolled)
 
else:
    print("\nThe number of times you chose to throw the dice was: ", numOfRolls)
    print("The number of items in the current array is: ", countArray)
    print("The sum of all the items in the current array is: ", sum(countArray))

