def welcome():
    print('''
Welcome to Python Calculator
''')


def calculate():
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ** for power
    % for modulo
    ''')

    number_1 = int(input('Enter your first number: '))
    number_2 = int(input('Enter your second number: '))

    if operation == '+':
        print(f'{number_1} + {number_2} = ')
        print(number_1 + number_2)

    elif operation == '-':
        print(f'{number_1} - {number_2} = ')
        print(number_1 - number_2)

    elif operation == '*':
        print(f'{number_1} * {number_2} = ')
        print(number_1 * number_2)

    elif operation == '/':
        print(f'{number_1} / {number_2} = ')
        print(number_1 / number_2)

    elif operation == '**':
        print(f'{number_1} ** {number_2} = ')
        print(number_1 ** number_2)

    elif operation == '%':
        print(f'{number_1} % {number_2} = ')
        print(number_1 % number_2)

    else:
        print('You have not typed a valid operator.')


def repeat():
    calc_repeat = input('''
Do you want to keep calculating?
Y/N.
''')

    if calc_repeat.upper() == 'Y':
        calculate()
        repeat()
    elif calc_repeat.upper() == 'N':
        print('Thank you! See you later.')
    else:
        repeat()


# Call funcs()
welcome()
calculate()
repeat()
