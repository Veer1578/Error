try:
    number = int(input('The entered number is:'))
    print('The entered number is', number)
except ValueError as ex:
    print('Exception:',ex )