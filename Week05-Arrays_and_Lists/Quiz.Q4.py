'''
Write a program that enters a string containing a person's full name and then output their initials. Example:

Full Name: Lachlan van der Velden
Initials: LVDV
Full Name: Dave Verg Douglas
Initials: DVD

'''
fullName = input('Enter your full name: ')

name = ''
for i,j in enumerate(fullName):
    if i == 0:
        name+=(j+'')
    elif j == ' ':
        name += (fullName[i+1]+'')

print(name.upper())