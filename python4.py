"""1. Write a Python program to reverse the content of the string.
Do not use built in 
"""
"""
print("Python program to reverse the content of the string.")
string = input("Enter the string:")
reversed_string = ''
length = len(string)
for i in range(length - 1, -1, -1):
        reversed_string += string[i]
print(reversed_string)
"""

"""
2. Create a program that performs basic string compression using the counts of repeated characters. For example, the string “aabcccccaaa” would become “a2b1c5a3”.

"""
"""
print("Basic string compression using the counts of repeated characters")
def compress_string(input_string):
    if not input_string:
        return ""

    compressed_string = ""
    count = 1
    length = len(input_string)

    for i in range(1, length):
        if input_string[i] == input_string[i - 1]:
            count += 1
        else:
            compressed_string += input_string[i - 1] + str(count)
            count = 1
    
    compressed_string += input_string[-1] + str(count)
    
    return compressed_string

input_string = "aabcccccaaa"
compressed = compress_string(input_string)
print("Original String:", input_string)
print("Compressed String:", compressed)

"""
"""
3. Get the Caesar cipher from the user Decrypt the cipher 

print("Get the Caesar cipher from the user Decrypt the cipher")
Caesar_cipher = input("Enter the Cipher text:")
"""
"""
def decrypt_caesar_cipher(cipher_text, shift):
    decrypted_message = ""
    
    # Normalize the shift to be within 0-25
    shift = shift % 26
    
    for char in cipher_text:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift
            
            if char.islower():
                # Decrypt lowercase letters
                start = ord('a')
                decrypted_char = chr((ord(char) - start - shift_amount) % 26 + start)
            elif char.isupper():
                # Decrypt uppercase letters
                start = ord('A')
                decrypted_char = chr((ord(char) - start - shift_amount) % 26 + start)
            
            decrypted_message += decrypted_char
        else:
            # Non-alphabetic characters are added unchanged
            decrypted_message += char
    
    return decrypted_message

# Get input from the user
cipher_text = input("Enter the Caesar cipher text to decrypt: ")
shift = int(input("Enter the shift value used for encryption: "))

# Decrypt the message
decrypted_message = decrypt_caesar_cipher(cipher_text, shift)
print("Decrypted Message:", decrypted_message)

"""
"""
4. Get the cipher encrypted using shift cipher. Identify the key used to encrypt using brute force 
   ie all the values in the key space 

5. Find the k value , Provided cipher text and plain text 
"""
def decrypt_caesar_cipher(cipher_text, shift):
    decrypted_message = ""
    shift = shift % 26  # Normalize shift to be within 0-25
    
    for char in cipher_text:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - start - shift) % 26 + start)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char  # Keep non-alphabetic characters unchanged
    
    return decrypted_message

def brute_force_caesar_cipher(cipher_text):
    for shift in range(26):
        decrypted_message = decrypt_caesar_cipher(cipher_text, shift)
        print(f"Shift {shift}: {decrypted_message}")

# Get input from the user
cipher_text = input("Enter the Caesar cipher text to decrypt: ")

# Perform brute force decryption
print("\nBrute Force Decryption Results:\n")
brute_force_caesar_cipher(cipher_text)

"""
6. Encrypt and decrypt the string using Atbash cipher 

7. Encrypt and decrypt using Affine cipher 
        add validation
"""
