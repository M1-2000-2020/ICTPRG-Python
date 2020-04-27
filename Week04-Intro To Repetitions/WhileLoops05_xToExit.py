print("Please press 'x' on the keyboard if you want to exit the program.")
sum1=0
num1=input("Please enter a number: ")

while num1 != "x":
	sum1=sum1+int(num1)
	num1=input("Please try another number: ")
	
print("Total: ", sum1)

