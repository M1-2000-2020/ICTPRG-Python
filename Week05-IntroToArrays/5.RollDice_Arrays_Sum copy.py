
import random
rolled = random.randint(1, 6)
CorrectFlag = True
totalCount = 1
countArray = []

while (totalCount <= 4 and CorrectFlag == True):
    rolled=int(input("How many times would you like to roll the dice? (number needs to be inbetween 1 - 4) : "))
    totalCount += 1
    countArray.append(rolled)
    
    if (totalCount >= 5 and CorrectFlag == True):
        print("Try again. You typed in a wrong number!")
    elif ():
        print("The dice rolled and you have thrown the number: ", rolled)
    else:
        CorrectFlag = False
        print("\nThe number of times you chose to throw the dice was: ", rolled)
        print("The number of items in the current array is: ", countArray)
        print("The sum of all the items in the current array is: ", sum(countArray))

