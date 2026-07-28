alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

# 1. Define functions FIRST
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            # Get current position
            current_pos = alphabet.index(letter)
            # Use % 26 to wrap around from 'z' back to 'a'
            new_pos = (current_pos + shift_amount) % 26
            cipher_text += alphabet[new_pos]
        else:
            # Keep spaces/symbols as they are
            cipher_text += letter
    print(f"Here is the encoded result: {cipher_text}")

# 2. Add your decrypt function logic here later!
def decrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter in alphabet:
            # Get current position
            current_pos = alphabet.index(letter)
            # Use % 26 to wrap around from 'z' back to 'a'
            new_pos = (current_pos - shift_amount) % 26
            cipher_text += alphabet[new_pos]
        else:
            # Keep spaces/symbols as they are
            cipher_text += letter
    print(f"Here is the decoded result: {cipher_text}")

# 3. Then run the logic
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    # You'll call decrypt(text, shift) once defined
    decrypt(text, shift)