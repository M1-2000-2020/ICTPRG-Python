'''

Write a program to ask the user for numbers, and then print any repeating numbers in a list. Example:

Enter a number: 5
Enter a number: 2
Enter a number: 6
Enter a number: 98
Enter a number: 7
Enter a number: 6
Enter a number: 5
Enter a number: x
Repeating numbers: [5, 6]

'''

print('Enter a number or x to exit')

num_list = []       # keep track of input numbers
repeat_num = set()     # a set to keep track of repeating number
num1 = input('Enter a number: ') 
while num1.lower() != 'x':
    if int(num1) in num_list:
        repeat_num.add(int(num1))
    num_list.append(int(num1))
    num1 = input('Enter a number: ')
print('Repeating numbers: ', list(repeat_num))