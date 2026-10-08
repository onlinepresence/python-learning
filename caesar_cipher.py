def caesar_cipher(text, shift, encrypt = True):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    if(not isinstance(shift, int)):
        return "Shift needs to be an integer"

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    # handle shift depending on encryption
    if not encrypt:
        shift = - shift

    shifted_alphabets = alphabets[shift:] + alphabets[:shift]

    # create a translation table
    translation_table = str.maketrans(alphabets + alphabets.upper(), shifted_alphabets + shifted_alphabets.upper())

    # return the translation
    return text.translate(translation_table)

# an encryption function
def encrypt(text, shift):
    return caesar_cipher(text, shift)

def decrypt(text, shift):
    return caesar_cipher(text, shift, False)

restart = True

while restart:
    print("\nWelcome to the CAESAR CIPHER program. We shall encrypt or decrypt a message for you")
    print("Select what you want to do:")
    print("1. I want to encrypt a text")
    print("2. I want to decrypt a text")
    print("3. Exit the program")
    encryption = int(input("Response: "))

    if encryption < 1 or encryption > 3:
        print("Invalid values provided. We needed a value between 1 and 3\n\n")
        continue

    if encryption == 3:
        print("\n\nThanks for trying us out. See you another time :D")
        break

    text = input("\nProvide your text\nResponse: ")
    shift = int(input("\nHow many shifts\nResponse: "))

    print("\n------------------------------------")
    print("Processing your request, please wait...\n")

    response = mode = ""

    if encryption == 1:
        response = encrypt(text, shift)
        mode = "encrypted"
    else:
        response = decrypt(text, shift)
        mode = "decrypted"

    print(f"Your '{text}' has been {mode} to: {response}")

    # continue or stop the loop
    print('\nWill you like to start over?\n1. Yes \t\t 2. No')
    restart = int(input("Response: "))

    if(restart == 1):
        print("\n\n")
        restart = True
    else: 
        print("\n\nThanks for trying us out. See you another time :D")
        restart = False

