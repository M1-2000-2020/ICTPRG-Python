
c_count = input("Please type in a sentence that includes capital C's and small letter c's: ")
print("The number of characters in this sentence is: ",len(c_count))
x = c_count.count('c')
y = c_count.count('C')
print("The Total number of C's and c's in the sentence is: ",x+y)
