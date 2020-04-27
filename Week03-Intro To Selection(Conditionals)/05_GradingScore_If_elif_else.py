mark = int(input("Enter your graded mark (0 - 100): "))

if (mark >= 101):
    print("Unfortunately you can not enter a number above 100!")
    
elif (mark >= 90):
    print("You have been graded a High Distinction! Well done!")
    
elif (mark >= 80):
    print("You have been graded a Distinction! Well done!")

elif (mark >= 70):
    print("You have been graded a Credit! Well done!")

elif (mark >= 50):
    print("You have been graded a Pass! Well done!")

else:
    print("Unfortunately you have not passed!")
    
    

