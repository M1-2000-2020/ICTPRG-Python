rows = int(input("Please enter how many rows you need to make up a square? "))
i = 0
while(i < rows):
    j = 0
    while(j < rows):      
        j = j + 1
        print('x', end='')
    i = i + 1
    print('')


rows = int(input("Please enter the total number of rows you need to make a right-angled triangle pattern: "))

i = 1
while(i <= rows):
    j = 1
    while(j <= i):
        print('x', end = '  ')
        j = j + 1
    i = i + 1
    print()
