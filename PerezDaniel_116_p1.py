# Filename: project_1.py

### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME: Daniel J Perez
# STUDENT ID: 802-18-9272
# SECTION: 116

############       ADD YOUR CODE BELOW        ############
def convert_decimal_to_base(decimal_number, base):
    remainder_track = ''
    decimal_number = int(decimal_number)
    if decimal_number == 0 or base == 10:
         return str(decimal_number)
    while decimal_number > 0:
        remaindern = decimal_number % base
        remainder = dec_to_hexdigit(remaindern)
        remainder_track = str(remainder)+remainder_track
        decimal_number = decimal_number // base
    return remainder_track




def convert_base_to_decimal(binary_number, base):
    remainder_track = 0
    exp = 0
    binary_number = str(binary_number)
    reverse_bnumber = binary_number[::-1]
    for bnumber in reverse_bnumber:
        hex_to_dec = hex_to_decdigit(bnumber)
        num = int(hex_to_dec)
        multiply_expo = num * base ** exp
        remainder_track += multiply_expo
        exp += 1
    return remainder_track



def convert_base1_to_base2(b1num, b1, b2):
    verification = True
    if b1 == 2 and b2 == 8:
        b1num = int(b1num)
        bi_dec = convert_base_to_decimal(b1num, b1)
        dec_base = convert_decimal_to_base(bi_dec, b2)
        return dec_base
    elif b1 == 2 and b2 == 16:
        b1num = int(b1num)
        bi_dec = convert_base_to_decimal(b1num, b1)
        dec_base = convert_decimal_to_base(bi_dec, b2)
        return dec_base
    elif b1 == 8 and b2 == 2:
        b1num = int(b1num)
        oct_dec = convert_base_to_decimal(b1num, b1)
        dec_base = convert_decimal_to_base(oct_dec, b2)
        return dec_base
    elif b1 == 8 and b2 == 16:
        b1num = int(b1num)
        oct_dec = convert_base_to_decimal(b1num, b1)
        dec_base = convert_decimal_to_base(oct_dec, b2)
        return dec_base
    elif b1 == 16 and b2 == 2:
        hex_base = convert_base_to_decimal(b1num, b1)
        dec_base = convert_decimal_to_base(hex_base, b2)
        return dec_base
    elif b1 == 16 and b2 == 8:
        hex_base = convert_base_to_decimal(b1num, b1)
        dec_base = convert_decimal_to_base(hex_base, b2)
        return dec_base
    else:
        print('Invalid base!')



def dec_to_hexdigit(num):
    if num >= 0 and num < 10:
        num = num
    elif num == 10:
        num = 'A'
    elif num == 11:
        num = 'B'
    elif num == 12:
        num = 'C'
    elif num == 13:
        num = 'D'
    elif num == 14:
        num = 'E'
    elif num == 15:
        num = 'F'
    return num


def hex_to_decdigit(num):
    # Changes numbers from hexadecimal to decimal (accepts lower and upper case letter)
    if num == 'A' or num == 'a':
        num = 10
    elif num == 'B' or num == 'b':
         num = 11
    elif num == 'C' or num == 'c':
        num = 12
    elif num == 'D' or num == 'd':
        num = 13
    elif num == 'E' or num == 'e':
        num = 14
    elif num == 'F' or num == 'f':
        num = 15
    else:
        # check is number are positive, if not it will print -1 (also checks for symbols or invalid letters)
        try:
            num = int(num)
            if num >= 0:
                num = str(num)
        except:
            num = -1
    return num

def check_base_to_decimal(bi_oc_hex, base):
    verification = True
    # This function verificates if the input number is a valid number for its base
    for check in bi_oc_hex:
        if base == 2:
            # checks if number is 0 or 1 for it to be valid
            check = int(check)
            if check > 1:
                print('Invalid Binary number!')
                verification = False
                break
        if base == 8:
            # checks if number is from 0-7 for it to be valid
            check = int(check)
            if check > 7:
                print('Invalid Octahedral number!')
                verification = False
                break
        if base == 16:
            # checks if number are not negative
            check = hex_to_decdigit(check)
            check = int(check)
            if check < 0:
                print('Invalid Hexahedral number!')
                verification = False
                break
            else:
                continue
    return verification


def process_conversion(numericOption):  # This function will process the valid  selections
    if numericOption == 1:
        dec_num = int(input("Enter the number to be converted: "))
        base = int(input('Enter the output base: '))
        if dec_num < 0:
            # checks if number is not negative
            print('Invalid number!')
        if base != 2 and base != 8 and base != 16:
            # check if input base are valid
            print('Invalid base!')
        else:
            bnumber = convert_decimal_to_base(dec_num, base)
            print("The decimal number " + str(dec_num) + ' is ' + bnumber + ' in base ' + str(base))

    if numericOption == 2:
        bi_oc_hex = input('Enter the number to be converted: ')
        base = int(input('Enter the input base: '))
        verification = check_base_to_decimal(bi_oc_hex, base)
        if verification == True:
            if base == 8 or base == 16 or base == 2:
                bnumber = convert_base_to_decimal(bi_oc_hex, base)
                print('The number ' + str(bi_oc_hex) + ' in base ' + str(base) + ' is ' + str(bnumber) + ' as a decimal.')
            else:
                print('Invalid base and/or number!')

    if numericOption == 3:
        base_num = input('Enter the number in its base: ')
        base_input = int(input('Enter the input base: '))
        base_output = int(input('Enter the output base: '))
        verification = check_base_to_decimal(base_num, base_input)
        if verification == True:
                bnumber = convert_base1_to_base2(base_num, base_input, base_output)
                if bnumber != None:
                    print('The number ' + str(base_num) + ' in base ' + str(base_input) + ' is ' + str(bnumber) + ' in base ' + str(base_output))


    if numericOption == 4:
        print('Thanks for using the base conversion program!')


def print_program_menu():
    print("\n--------")
    print("Welcome to the base conversion program. Please, choose an option:")
    print("1. Decimal to Binary, Octal or Hexadecimal")
    print("2. Binary, Octal or Hexadecimal to Decimal")
    print("3. Binary, Octal or Hexadecimal to Binary, Octal or Hexadecimal")
    print("4. Exit")


# This function verify if the entered option is an integer
def identify_option(option):
    # Verify that a number was input and it is in valide renge
    try:
        numericOption = int(option)
        return numericOption
    except:
        return -1  # invalid option


def main():
    done = False
    while not done:
        print_program_menu()
        userOption = input('Enter option: ')
        optionInfo = identify_option(userOption)
        if optionInfo != -1:
            # Invalid option
            if optionInfo == 4:
                done = True
                print('Thanks for using the number conversion program!')
            else:
                process_conversion(optionInfo)
        else:
            # Option was invalid
            print('Invalid oprion\n')


# This line makes python start the program from the main function
if __name__ == "__main__":
    main()

