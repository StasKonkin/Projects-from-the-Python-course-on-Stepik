# Setting up the Russian and English alphabets
alph_ru = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'.lower()
alph_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()

# Asking for user's name
name = input("Enter your name: ")

# Greeting message
print(f'Hello, {name.capitalize()}! I am the Caesar Cipher Encryptor/Decryptor, and I can encrypt or decrypt any text.')

# Function to check user's choice for encryption or decryption
def check_ciphers():
    while True:
        ciphers = input('Choose an action: encrypt - enter 1; decrypt - enter 2... ')
        if ciphers != '1' and ciphers != '2':
            print("Input error...")
        elif ciphers == '1':
            ciphers = 1
            return ciphers
        else:
            ciphers = 2
            return ciphers

# Function to check user's choice for language
def check_language():
    while True:
        language = input('Choose the language of the text: Russian - enter ru; English - enter en... ')
        if language != 'ru' and language != 'en':
            print("Input error...")
        elif language == 'ru':
            language = alph_ru
            return language
        else:
            language = alph_en
            return language

# Function to check the shift step
def check_step():
    while True:
        step = input('Enter the shift step... ')
        if not step.isdigit():
            print("Input error...")
        else:
            step = int(step)
            return step

# Checking user's choices
ciphers = check_ciphers()
language = check_language()
step = check_step()

# Getting user's text
text = input('Enter your text... ')

# Encrypting or decrypting the text
answer = ''
for i in text:
    if i.lower() in language:  # Only letters will be shifted
        if ciphers == 2:  # Decryption code with preserving case
            if i.isupper():  # Checking case
                answer += language[language.find(i.lower()) - step].upper()  # Finding the letter and shifting it in the alphabet
            else:
                answer += language[language.find(i.lower()) - step]
        else:  # Encryption code with preserving case
            if language.find(i.lower()) + step >= len(language):  # Checking if the character goes beyond the limits, if yes, subtract the alphabet length
                if i.isupper():
                    answer += language[language.find(i.lower()) + step - len(language)].upper()
                else:
                    answer += language[language.find(i.lower()) + step - len(language)]
            else:
                if i.isupper():
                    answer += language[language.find(i.lower()) + step].upper()
                else:
                    answer += language[language.find(i.lower()) + step]
    else:  # Non-letters will be left as is
        answer += i

# Printing the result
print(answer)
