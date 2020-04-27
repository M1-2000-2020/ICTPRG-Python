# rolling the dice
import random
min_num=1
max_num=6
countarray=[]
#select the number of times you want to roll the dice
print("How many numbers do you want to roll?")
roll=int(input())
#print(roll)
#initiate sum of numbers selected
i=0
sum=0
while i < roll:
    print("Rolling the dice")
    diceroll=random.randint(min_num,max_num)
    print("The number randomly generated is",diceroll)
    print("Indicate whether you want this to be counted (y or n)")
    option=input()
    if option == "y" :
        countarray.append(diceroll)
        print("The number",diceroll,  "is selected  ")
        sum=sum + diceroll
    i=i+1
print("The sum of the numbers selected is", sum)
print("The numbers selected are ", countarray)