alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

def encrypt(original_text, shift_amount):
    cipher_text = ""

    # TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position = shifted_position % len(alphabet)  ## Let's say the letter is 'z', which is at index 25
                                                            ## If we shift it by 9 → 25 + 9 = 34
                                                            ## But our alphabet only has 26 letters, index goes from 0 to 25
                                                            ## So 34 goes out of range and would normally cause an error
                                                            ## Here's where modulo comes in: 34 % 26 = 8 → meaning 26 fits into 34 once,
                                                            ## and the leftover (the remainder) is 8
                                                            ## That brings us back to index 8, which is the letter 'i'
                                                            ## It's like wrapping around the alphabet when we go past 'z'

        #or shifted_position %= len(alphabet)

        cipher_text += alphabet[shifted_position]

    print(f"Here is encoded result: {cipher_text}")


# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(original_text=text, shift_amount=shift)