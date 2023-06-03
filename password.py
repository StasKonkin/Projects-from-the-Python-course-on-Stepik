# This code generates a password based on user preferences 
# for its length and the inclusion of different character types 
# (digits, lowercase letters, uppercase letters, and symbols).
from random import *
digits_num = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!@#$%^&*()_+-<>/\|?'

# Functions to ask about password preferences 

def check_len_password(): # min len - 7 symbols
    while True:
        len = input('Enter the length of the password... (minimum 7 characters): ')
        if not len.isdigit():
            print("Input error...")
        else:
            if int(len) >= 7:
                return int(len)
            else:
                print("Input error...")

def check_digit():
    while True:
        digit = input('Shall the numbers be included 0123456789? (y/n)')
        if digit != 'y' and digit != 'n':
            print("Input error...")
        elif digit == 'y':
            digit = 1
            return digit
        else:
            digit = 0
            return digit

def check_upper():
    while True:
        upper  = input('Shall the uppercase letters (ABCDEFGHIJKLMNOPQRSTUVWXYZ) be included? (y/n)')
        if upper != 'y' and upper != 'n':
            print("Input error...")
        elif upper == 'y':
            upper = 1
            return upper
        else:
            upper = 0
            return upper

def check_lower():
    while True:
        lower = input('Shall the lowercase letters (abcdefghijklmnopqrstuvwxyz) be included? (y/n)')
        if lower != 'y' and lower != 'n':
            print("Input error...")
        elif lower == 'y':
            lower = 1
            return lower
        else:
            lower = 0
            return lower

def check_symbols():
    while True:
        symbols = input('Shall the symbols (!#$%&*+-=?@^_?) be included (y/n)')
        if symbols != 'y' and symbols != 'n':
            print("Input error...")
        elif symbols == 'y':
            symbols = 1
            return symbols
        else:
            symbols = 0
            return symbols

# Main function
len = check_len_password()
digit = check_digit()
upper = check_upper()
lower = check_lower()
symbols = check_symbols()
# adding all the requested features by one of each
password = digit * choice(digits_num) + upper * choice(uppercase_letters) + lower * choice(lowercase_letters) + symbols * choice(punctuation) 
chars =  digit*digits_num + upper*uppercase_letters + lower*lowercase_letters + symbols*punctuation # string of all possible chars (only types that were approved)
password += ''.join(sample(chars, len - digit - upper - lower - symbols)) # adding symbols to the requested lengthn
password_list = list(password)
shuffle(password_list)
print("Your generated password is: ", *password_list, sep='')
