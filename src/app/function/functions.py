import random 
import pyperclip

def generate_password(length, include_numbers):
    """
    This is a function which will generate
    random password depend on the arguments

    Args:
        length ([int]): [This argument specifies the length of the password]
        include_numbers ([boolean]): [This argument specifies whether numbers 
        shoulb be included or not]

    Returns:
        [string]: [This function returns the randomly generated password]
    """
    characters_array = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers_array = "1234567890"
    password = ""

    if (include_numbers):
        half_length = length // 2
        rest_num = length - half_length
        
        for i in range(0, half_length):
            index = random.randint(0, len(characters_array)-1)
            password += characters_array[index]

        for i in range(0, rest_num):
            index = random.randint(0, len(numbers_array)-1)
            password += numbers_array[index]

        return password

    for i in range(0, length):
        index = random.randint(0, len(characters_array)-1)
        password += characters_array[index]

    return password

def copy_to_clipboard(text):
    """
    This is a function which copies the text which is passed to the clipboard

    Args:
        text ([string]): [This argument specifies the text which has to be copied]
    """
    pyperclip.copy(text=text)