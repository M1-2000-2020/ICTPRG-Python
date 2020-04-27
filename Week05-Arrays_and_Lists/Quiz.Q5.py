'''
Write a program that can accept many numbers from the user, until they enter an x. Example:

Enter a number: 5
Enter a number: 9
Enter a number: 3
Enter a number: 12
Enter a number: x
You entered: [9, 3, 12]
'''

print("Please press 'x' on the keyboard if you want to exit the program.")
sum1=0
num1=input("Please enter a number: ")
items = []

while num1 != "x":
	sum1=sum1+int(num1)
	items.append(int(num1))
	num1=input("Enter another number - ('x' exits): ")
		
print("Total: ", sum1)
print("All the numbers you chose: ", items)
