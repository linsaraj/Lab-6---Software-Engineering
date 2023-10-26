# Sara Lin

# encoder
def encoder(password):

    revised_password = ''
    # empty string

    for i in password:
        # adds +3 to each digit
        variable = int(i) + 3
        revised_password += str(variable)
        # adds the variable to an empty string

    return revised_password

# decoder
def decoder(password):
    pass

condition = True
while condition == True:

    print()
    print('Menu:')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')
    print()
    # the menu options

    user_input = int(input('Please enter an option: '))

    if user_input == 1:
        # encode option

        password = input('Please enter your password to encode: ')

        if len(password) < 8:
            # if the password is less than 8 digits, it prompts the user to reenter password
            print('Your password should be at least 8 digits long.')
            continue

        revised_password = encoder(password)
        # encodes the password and stores it
        print('Your password has been encoded and stored!')

    if user_input == 2:
        # decode option
        password = decoder(revised_password)
        # decodes the password
        print(f'The encoded password is {revised_password}, and the original password is {password}.')

    if user_input == 3:
        # exit option
        break
