try:
    num1, num2 = eval(input('Enter 2 numbers seperated by a comma: '))
    result = num1 / num2
    print(f'The result is {result}')
except ZeroDivisionError:
    print('Division by zero is not allowed')
except SyntaxError:
    print('You have to seperate the entered numbers with a comma')
except:
    print('Wrong input')
else:
    print('No exceptions')
finally:
    print('This will print no matter what')