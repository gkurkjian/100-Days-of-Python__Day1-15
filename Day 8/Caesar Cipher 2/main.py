### My version. Calling the functions by its names


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.

# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
def decrypt(original_text, shift_amount):
    ciper_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        ciper_text += alphabet[shifted_position]
    print(f"Here is the decrypted result: {ciper_text}")

#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def encrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {output_text}")

def caesar(original_text, shift_amount, encode_or_decode):
    if direction == 'encode':
        encrypt(original_text=text, shift_amount=shift)
    elif direction == 'decode':
        decrypt(original_text=text, shift_amount=shift)
    else:
        print("Have a wonderful luck my dear. Byeee!")

caesar(direction, text, shift)

# encrypt(original_text=text, shift_amount=shift)
# decrypt(original_text=text, shift_amount=shift)