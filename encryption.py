# encryption.py
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.

import string # Import string module from the standard Python Library

def cipher_valid(cipher):
    '''
    Validates cipher, ensuring that it is not greater or less than 26 characters.

    Arguments:
    cipher_text -- users input cipher

    Returns:
    If the cipher is 26 chracters, returns the string 'Your cipher is valid.'.
    '''
    if len(cipher) > 26 or len(cipher) < 26: # Ensures length of cipher is exacty 26.
        print('Your cipher must contain 26 unique elements of a-z or 0-9.\n')
    else :
        print('Your cipher is valid.')
        return 'Your cipher is valid.'

def bonus(cipher):
    '''
    Ensures the user inputted cipher is lowercase while removing all duplicates in the string.

    Arguments:
    cipher_text -- users input cipher

    Returns:
    Returns a string with lowercased alphabet (where applicable) and no duplicates (all unique characters).
    '''
    bonus_cipher = cipher.lower() # Makes the cipher lowercased.
    res_cipher = '' # An empty string to add unique characters of the cipher into to ensure no duplicates.
    for char in bonus_cipher:
        if char not in res_cipher: # If a character in the lowercased cipher (bonus_cipher) is not in the intially empty string, put it in the string (res_cipher).
            res_cipher += char
    return res_cipher # Return the string of unique characters.

def decode(cipher, processed, lower):
    '''
    Takes users inputted text to be decoded along with the user inputted cipher and creates a dictionary mapping the cipher characters (keys) to the lower case alphabet (values). Decodes the text inputted to be decoded.

    Arguments:
    cipher_text -- users input cipher
    to_be_processed -- users inputted text to be processed (encoded or decoded)
    lower_list -- list of the lowercase alphabet

    Returns:
    Returns the decoded version of the user inputted 'string to be decoded' (to_be_processed).
    '''
    lower_dict = dict(zip(cipher, lower)) # Creates a dictionary with the characters of the cipher as keys, and the lower cased alphabet as values (dictionary with 2 lists).
    decoded = '' # Empty string to add the decoded characters.
    for char in processed:
        decoded += lower_dict[char] # Decodes the characters of the to_be_processed string and adds them to intially empty string (decoded).
    return decoded # Returns the decoded string.

def encode(cipher, processed, lower):
    '''
    Takes users inputted text to be encoded along with the user inputted cipher and creates a dictionary mapping the lower case alphabet (keys) to the cipher characters (value). Encodes the text inputted to be encoded.

    Arguments:
    cipher_text -- users input cipher
    to_be_processed -- users inputted text to be processed (encoded or decoded)
    lower_list -- list of the lowercase alphabet

    Returns:
    Returns the encoded version of the user inputted 'string to be encoded' (to_be_processed).
    '''
    lower_dict = dict(zip(lower, cipher)) # Creates a dictionary with the characters of the cipher as values, and the lower cased alphabet as keys (dictionary with 2 lists).
    encoded = '' # Empty string to add the encoded characters.
    for char in processed:
        encoded += lower_dict[char] # Encodes the characters of the to_be_processed string and adds them to the intially empty string (encoded).
    return encoded # Returns the encoded string.


lower_list = list(string.ascii_lowercase) # Use string module to create a list of lowercase alphabet.
print('ENDG 233 Encryption Program') # Introduction of program.
user_choice = int(input('Select 1 to encode or 2 to decode your message, select 0 to quit: ')) # Prompt user's choice of action.

while True:
    if user_choice == 1 : # If true, execute all code related to encoding.
        to_be_processed = input('Please enter the text to be processed: ') # Prompt users text to be processed.
        cipher_input = input('Please enter the cipher text: ') # Prompt users cipher.
        cipher_text = bonus(cipher_input) # Call bonus function to execute code for 'Optional Bonus' requirements.
        if cipher_text.isalnum() == True or cipher_text.islower() == True: # Ensuring cipher is lowercase and/or alpha numeric.
            if cipher_valid(cipher_text) == 'Your cipher is valid.': # If cipher is valid, continue.
                print(f'Your output is: {encode(cipher_text, to_be_processed, lower_list)}\n') # Call encoding function, passing in the cipher input, text to be processed, and the list of the lowercase alphabet.
        user_choice = int(input('Select 1 to encode or 2 to decode your message, select 0 to quit: ')) # If cipher is not lowercase and or alphanumeric, prompt user input again until quit.
    elif user_choice == 2 : # If true, execute all code related to decoding.
        to_be_processed = input('Please enter the text to be processed: ') # Prompt users text to be processed.
        cipher_input = input('Please enter the cipher text: ') # Prompt users cipher.
        cipher_text = bonus(cipher_input) # Call bonus function to execute code for 'Optional Bonus' requirements.
        if cipher_text.isalnum() == True or cipher_text.islower() == True: # Ensuring cipher is lowercase and/or alpha numeric.
            if cipher_valid(cipher_text) == 'Your cipher is valid.': # If cipher is valid, continue.
                print(f'Your output is: {decode(cipher_text, to_be_processed, lower_list)}\n') # Call decoding function, passing in the cipher input, text to be processed, and the list of the lowercase alphabet.
        user_choice = int(input('Select 1 to encode or 2 to decode your message, select 0 to quit: ')) # If cipher is not lowercase and or alphanumeric, prompt user input again until quit.
    elif user_choice == 0 : # If true, executes code to exit program.
        print('Thank you for using the encryption program.\n')
        break # Breaks loop and exit's program.
