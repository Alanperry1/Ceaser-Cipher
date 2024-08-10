# Define the alphabet twice to handle shifts beyond 'z'
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

# Display the title art
print("""
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88
              88
              88
""")

# Start the main loop
continue_program = True
while continue_program:
    print("Type 'encode' to encrypt, type 'decode' to decrypt")
    mode = input().lower()  # Get the mode (encode or decode)

    print("Type your message")
    message = input().lower()  # Get the message to encode or decode

    print("Type the shift number")
    shift_value = int(input())  # Get the shift value

    # Ensure the shift value is within the range of the alphabet
    if shift_value > 26:
        shift_value %= 26


    # Define the Caesar Cipher function
    def caesar_cipher(input_text, shift_amount, mode_type):
        cipher_text = ""  # Initialize the result string

        # Determine if we are encoding or decoding
        if mode_type == "encode":
            operation = "encoded"
        elif mode_type == "decode":
            shift_amount = -shift_value  # Reverse the shift for decoding
            operation = "decoded"

        # Process each letter in the input text
        for letter in input_text:
            if letter in alphabet:
                old_position = alphabet.index(letter)  # Find the position of the letter in the alphabet
                new_position = old_position + shift_amount  # Apply the shift
                cipher_text += alphabet[new_position]  # Append the shifted letter to the result
            else:
                cipher_text += letter  # If not in the alphabet, just add the letter as is

        print(f'Your {operation} text is: {cipher_text}')


    # Call the Caesar Cipher function with the provided inputs
    caesar_cipher(message, shift_value, mode)

    # Ask the user if they want to go again
    print("Type 'yes' if you want to go again. Otherwise type 'no'.")
    play_again = input().lower()

    if play_again == "no":
        continue_program = False  # Exit the loop if the user doesn't want to continue
        print("Goodbye!")
