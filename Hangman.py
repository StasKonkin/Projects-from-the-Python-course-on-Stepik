from random import choice

word_list = [
    'apple', 'banana', 'cherry', 'date', 'elderberry',
    'fig', 'grape', 'kiwi', 'lemon', 'mango',
    'orange', 'pear', 'quince', 'raspberry', 'strawberry',
    'watermelon', 'aeroplane', 'butterfly', 'castle', 'dolphin',
    'elephant', 'fireworks', 'guitar', 'hamburger', 'island',
    'jigsaw', 'kangaroo', 'lighthouse', 'mountain', 'nightingale',
    'ocean', 'piano', 'queen', 'rainbow', 'seashell',
    'tiger', 'umbrella', 'volcano', 'waterfall', 'xylophone',
    'yacht', 'zebra', 'carrot', 'laptop', 'rain',
    'sunflower', 'football', 'book', 'dog', 'cat'
]


def get_word():
    word = choice(word_list).upper()
    return word


# Function to display the current hangman state
def display_hangman(tries):
    stages = [  # Final stages: head, torso, both arms, both legs
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # Head, torso, both arms, one leg
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # Head, torso, both arms
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # Head, torso, and one arm
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # Head and torso
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # Head only
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # Initial state
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]


def play(word):
    word_completion = ['_' for _ in range(len(word))]  # String containing '_' for each letter in the word
    guessed = False
    guessed_letters = []  # List of already guessed letters
    guessed_words = []  # List of already guessed words
    tries = 6  # Number of allowed tries
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print("Number of remaining tries:", tries)
    print(*word_completion, sep=' ')
    print()

    while not guessed and tries > 0:
        guess = input("Enter a letter: ").upper()

        if guess.isalpha() and len(guess) == 1 and guess not in guessed_letters:
            # Check if the input is a single alphabetical letter that hasn't been guessed before
            guessed_letters.append(guess)  # Add the guessed letter to the list of guessed letters

            if guess in word:
                # The guessed letter is in the word
                print("Correct guess!")

                # Update the word completion with the guessed letter in the correct positions
                for i in range(len(word)):
                    if guess == word[i]:
                        word_completion[i] = guess

                print(*word_completion, sep=' ')
                print()

                if ''.join(word_completion) == word.upper():
                    # All letters have been guessed correctly
                    print("Congratulations! You won!!! Remaining tries:", tries)
                    break
            else:
                # The guessed letter is not in the word
                tries -= 1  # Reduce the remaining tries
                print("Wrong guess! Remaining tries:", tries)
                print(display_hangman(tries))
                print(*word_completion, sep=' ')
                print()
        elif guess in guessed_letters:
            # The letter has already been guessed before
            print("Input error! This letter has already been guessed.")
        else:
            # The input is not a valid single alphabetical letter
            print("Input error! Only letters of the English alphabet are accepted.")

    if tries == 0:
        # Player has run out of tries
        print("Unfortunately, you lost!")
        print("The correct word was:", word)


word = get_word()
play(word)
