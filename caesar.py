import string
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    answer = ""
    count = 0

    """Check user input for a valid integer"""
    try:
        rot = int(rot)
    except ValueError:
        while rot.isnumeric() == False and count < 10:
            rot = input("ERROR!  Please enter a valid integer: ")
            count = count + 1
        print("Program could not run.")
        return(answer)

    for i in range(len(text)):
        ltr = rotate_character(text[i], rot)
        answer = answer + ltr

    return(answer)

def main():
    text_input = input("Type a message: \n")
    rotation_input = input("Rotate by: \n")

    encrypt(text_input, rotation_input)

if __name__ == "__main__":
    main()