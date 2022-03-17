

def temp_calc():

    print()


while True:

    while True:
        print('Welcome to the Temperature Converter!')
        print('=' * 40)
        user_input = input('Enter F for Fahrenheit or C for Celsius: ')
        conv_type = user_input[0].lower()
        if conv_type in ['f', 'c']:
            break
        else:
            print('Please enter an F or a C.')

    while True:
        start_temp = int(input('Enter the starting temperature (-50 to 150)..: '))
        if -50 <= start_temp <= 150:
            break
        else:
            print('Please select a temperature between -50 and 150!')

    while True:
        stop_temp = int(input('Enter the stopping temperature (-50 to 150)..: '))
        if -50 <= stop_temp <= 150:
            break
        else:
            print('Please select a temperature between -50 and 150!')

    while True:
        step_temp = int(input('Enter the stepping temperature (-50 to 150)..: '))
        if -50 <= step_temp <= 50:
            break
        else:
            print('Please select a temperature between -50 and 150!')

    print()
    print('|=====|=====|')
    if conv_type == 'f':
        print('|  F  |  C  |')
        print('|=====|=====|')
    else:
        print('|  C  |  F  |')
        print('|=====|=====|')

    for temp in range(start_temp, stop_temp+1, step_temp):
        if conv_type == 'f':
            convert_temp = (temp - 32) * 5 / 9
        else:
            convert_temp = temp * 9 / 5 + 32

        print(f'| {temp:3.0f} | {convert_temp:3.0f} |')
    print('|=====|=====|')
    print()

    while True:
        user_input = input('Do you want to display another temperature chart (y/n)? ')
        contin = user_input[0].lower()
        if contin in ['y', 'n']:
            break
        else:
            print('Please enter a y or an n.')

    if contin == 'n':
        print()
        print('=' * 40)
        print('Thanks for playing!!')
        break
    else:
        print()


if __name__ == '__main__':
    temp_calc()
