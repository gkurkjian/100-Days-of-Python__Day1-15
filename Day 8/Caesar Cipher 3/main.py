# TODO-1: Import and print the logo from art.py when the program starts.
import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1  ## flip the procedure according to input 'encode' don't do anything, 'decode' do the following

    for letter in original_text:
        if letter not in alphabet:  ## if the symbol or character are not in the alphabet list
            output_text += letter  ## store it in output_text
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# TODO-3: Can you figure out a way to restart the cipher program?
should_continue = True  ## initiating the game to be True

while should_continue:  ## while the game is True; do the following
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()  ## fetch the value of direction

    while direction not in ['encode', 'decode']:  ## while loop through and check if direction doesn't match
        print("Invalid input. Please follow the instruction")  ## prompt error msg
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower() ## ask again until proper answer

    text = input("Type your message:\n").lower()  ## fetch the text of wish of the user
    shift = int(input("Type the shift number:\n"))  ## fetch the position of wish of the user

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)  ## pass the info to caesar function

    ## here we're prompting the user if they wish to continue to the game to restart
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower() ## prompt the user to continue
    while restart not in ['yes', 'no']:  ## while loop through of the answer if is 'yes' or 'no'
        print("Invalid input. Please follow the instruction")  ## prompt error msg
        restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.").lower() ## as again until proper answer

    if restart == 'yes':  ## if 'yes' to continue
        should_continue = True  ## keep going
    elif restart == 'no':  ## if 'no' to continue
        print("goodbye!")  ## goodbye msg
        should_continue = False  ## stop the code, exit

