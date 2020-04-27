'''
Given the following python code:

values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
Sum all of the numbers and output the result
Average all of the numbers and output the result
Output the maximum number in the list

'''
values = [89, 456, 4, 55, 232, 2, 54, 78, 65, 45, 12, 459, 35616, 45 ,78]
print (sum(values))
avg = (sum(values)/len(values))
print (avg) 
length = len(values)
values.sort()
print(values) 
print("Largest element is: ",values[length-1])    
