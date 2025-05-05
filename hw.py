try:
    age = int(input('Enter a number: '))
    if age % 2 == 0:
        print('Even')
    else:
        print('Odd')
except ValueError:
    print('Invalid')