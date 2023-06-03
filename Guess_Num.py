# Importing necessary libraries
from random import *
from math import log2, ceil

# Function to check if the input is a valid number
def is_valid(num):
    answer = False
    if num.isdigit():
        if 1 <= int(num) <= 100:
            answer = True
    return answer

# Generating a secret number
secret = randint(1, 100)

# Printing the welcome message
print('Welcome to the Number Guessing Game')

# Getting user input
num = input('Enter an integer between 1 and 100: ')

# Initializing the counter
counter = 1

# Main game loop
while True:
    # Checking if the input is valid
    if not is_valid(num):
        print('Maybe we should try entering an integer between 1 and 100?')
        num = input()
        continue
    
    num = int(num)
    
    # Comparing the user's guess with the secret number
    if num > secret:
        print('Your number is greater than the secret number, try again')
        num = input()
        counter += 1
    elif num < secret:
        print('Your number is less than the secret number, try again')
        num = input()
        counter += 1
    else:
        # User has guessed the correct number
        print('Congratulations, you guessed it! The correct answer is:', secret)
        print("Total attempts:", counter)
        print("The problem could have been solved in ", ceil(log2(100)), "attempts.")
        print('Thank you for playing the Number Guessing Game. See you again...')
        break
