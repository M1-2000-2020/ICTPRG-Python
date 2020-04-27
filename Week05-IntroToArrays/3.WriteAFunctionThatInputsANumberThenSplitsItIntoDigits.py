'''
Write a function that takes a number and returns a list of its digits. So for 2342 it should return [2,3,4,2].
[int(x) for x in str(num)]
'''

def digitsReturn():
    num1 = input("Please enter a number more than one digit long: ")
    digits = [int(x) for x in str(num1)]
    print(digits)
digitsReturn()