import string

# Define the alphabet as lowercase letters
alphabet = string.ascii_lowercase 

# Get user input for encryption or decryption mode
encrypt_mode = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()

# Get the shift number and convert it to an integer
shift_number = int(input("Type the shift number: "))

# Get the message to encrypt or decrypt, converted to lowercase
message = input("Type your message: ").lower()

# Initialize variables for storing results
encrypt_array = []  # Stores encrypted characters
encrypt_word = ''   # Stores final encrypted message
decrypt_word = ''   # Stores final decrypted message

# Function to encrypt the message
def encrypt():
    for letter in message:
        if letter in alphabet:
            # Find new shifted index and wrap around using modulo
            new_index = (alphabet.index(letter) + shift_number) % len(alphabet)
            encrypt_array.append(alphabet[new_index])  # Append encrypted letter
        else:
            encrypt_array.append(letter)  # Append non-alphabet characters unchanged
        
        # Join the encrypted letters into a single string
        encrypt_word = "".join(encrypt_array)
    
    # Print the encrypted message
    print(f'Here is the encoded result: {encrypt_word}')

# Function to decrypt the message
def decrypt():
    for letter in message:
        if letter in alphabet:
            # Find new shifted index for decryption (shifting backwards)
            new_index = (alphabet.index(letter) - shift_number) % len(alphabet)
            encrypt_array.append(alphabet[new_index])  # Append decrypted letter
        else:
            encrypt_array.append(letter)  # Append non-alphabet characters unchanged
        
        # Join the decrypted letters into a single string
        decrypt_word = "".join(encrypt_array)
    
    # Print the decrypted message
    print(f'Here is the decoded result: {decrypt_word}')

# Check user input and call the appropriate function
if encrypt_mode == 'encode':
    encrypt()
elif encrypt_mode == 'decode':
    decrypt()
else:
    encrypt_mode  # No action, but the variable remains assigned
