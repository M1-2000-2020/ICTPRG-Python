'''
Design a program which will ask the user to enter the date in the form dd/mm/yyyy. Example 23/08/2019

The date will be printed like below:

Date: 23
Month : 08
Year: 2019
'''

from itertools import groupby

dateToday = input("Please enter the current date in the format dd/mm/yyyy: ")
print("The date is: " + dateToday)
print("I am now separating the numbers from the date and placing them in an array.")
getNumbers = [''.join(j).strip() for sub in dateToday for k, j in groupby(sub, str.isdigit)] 
print ("The elements put in the array: " + str(getNumbers))

print("The day is: " + getNumbers[0]+getNumbers[1])
print("The month is: " + getNumbers[3]+getNumbers[4])
print("The year is: " + getNumbers[6]+getNumbers[7]+getNumbers[8]+getNumbers[9])
