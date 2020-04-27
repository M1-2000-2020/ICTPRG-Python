'''
Write a program that asks the user for a large number, and then sums all of the digits in that number: Example:

Enter a large number: 29834892
Sum of the digits: 2 + 9 + 8 + 3 + 4 + 8 + 9 + 2 = 45

'''

num1 = input("Please enter a large number, more than six digits long: ")
digits = [int(x) for x in str(num1)]
print(digits)
print(sum(digits))