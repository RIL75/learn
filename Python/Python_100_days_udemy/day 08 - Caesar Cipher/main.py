alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number\n"))


# TODO-1: create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift yount and print the encrpted text


def encrypt(original_text, shift_amount):


# TODO-3: Call the 'encrypt()' function and  pass in the user inputs.
#  You should be able to test the code and encrypt a message

#TODO-4: What happns if you try to shift z forwards by 9? Can you fix the code?

