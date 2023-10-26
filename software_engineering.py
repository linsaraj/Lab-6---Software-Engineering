# Sara Lin

# encoder
def encoder(password):

    revised_password = ''
    # empty string

    for i in password:
        # adds +3 to each digit
        if int(i) <= 6:
            variable = int(i) + 3
        if int(i) == 7:
            # if digit equals 7, 7+3=10, so new digit would be 0
            variable = 0
        if int(i) == 8:
            # if digit equals 8, 8+3=11, so new digit would be 1
            variable = 1
        if int(i) == 9:
            # if digit equals 9, 9+3=12, so new digit would be 2
            variable = 2
        revised_password += str(variable)
        # adds the variable to an empty string

    return revised_password

# decoder
def decoder(encoded_password):
        decoded_password = ""
        for digit in encoded_password:
            if int(digit) >= 3:
                decoded_digit = int(digit) - 3
            if int(digit) == 2:
                decoded_digit = 9
            if int(digit) == 1:
                decoded_digit = 8
            if int(digit) == 0:
                decoded_digit = 7
            decoded_password += str(decoded_digit)
        return(decoded_password)


if __name__ == '__main__':

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
