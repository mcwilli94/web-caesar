import string

def alphabet_position(letter):
    value = 0
    letter = letter.upper()
    Capital = string.ascii_uppercase

    for i in range(len(Capital)):
        if letter == Capital[i]:
            value = ord(Capital[i]) - 65

    return value

def rotate_character(char, rot):
    """Checks to see if the answer is a string data type and Checks to see if
    the string in an actual letter.  Rotates the letter within 26 if it is an
    actual letter"""
    if type(char) is str and char.isalpha() == True:
        char_value = alphabet_position(char)
        char_position = (char_value + rot) % 26
        if ord(char) < 96:
            return chr(char_position + 65)
        else:
            return chr(char_position + 97)
    else:  #if answer is not a letter, returns the answer
        return char