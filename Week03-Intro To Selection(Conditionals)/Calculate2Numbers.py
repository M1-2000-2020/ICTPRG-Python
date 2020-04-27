multiply = '*'
divide = '/'
subtract = '-'
addition = '+'
power = '**'
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
mathSymbol = input("Calculate by choosing one of the following math symbols; + - * / ** ")
if mathSymbol == multiply:
    print(num1 * num2)
if mathSymbol == divide:
    print(num1 / num2)
if mathSymbol == subtract:
    print(num1 - num2)
if mathSymbol == addition:
    print(num1 + num2)
if mathSymbol == power:
    print(num1 ** num2)

 