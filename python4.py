"""1. Write a Python program to reverse the content of the string.
Do not use built in 
"""

print("Python program to reverse the content of the string.")
string = input("Enter the string:")
reversed_string = ''
length = len(string)
for i in range(length - 1, -1, -1):
        reversed_string += string[i]
print(reversed_string)

"""
2. Create a program that performs basic string compression using the counts of repeated characters. For example, the string “aabcccccaaa” would become “a2b1c5a3”.
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
3. Get the Caesar cipher from the user Decrypt the cipher 
"""

print("Get the Caesar cipher from the user Decrypt the cipher")
Caesar_cipher = input("Enter the Cipher text:")

def decrypt_caesar_cipher(cipher_text, shift):
    decrypted_message = ""

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
            decrypted_message += char
    
    return decrypted_message

cipher_text = input("Enter the Caesar cipher text to decrypt: ")
shift = int(input("Enter the shift value used for encryption: "))

decrypted_message = decrypt_caesar_cipher(cipher_text, shift)
print("Decrypted Message:", decrypted_message)


"""
4. Get the cipher encrypted using shift cipher. Identify the key used to encrypt using brute force 
   ie all the values in the key space 
"""
def shift_cipher_encrypt(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(encrypted_char)
        else:
            result.append(char)
    return ''.join(result)

def shift_cipher_decrypt(text, shift):
    return shift_cipher_encrypt(text, -shift)

def brute_force_decrypt(cipher_text):
    for shift in range(1, 26):
        decrypted_text = shift_cipher_decrypt(cipher_text, shift)
        print(f"Shift {shift}: {decrypted_text}")

encrypted_text = "Khoor Zruog"  # Encrypted with a shift of 3
print("Encrypted Text:", encrypted_text)

print("\nBrute-force decryption results:")
brute_force_decrypt(encrypted_text)

"""
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

cipher_text = input("Enter the Caesar cipher text to decrypt: ")

print("\nBrute Force Decryption Results:\n")
brute_force_caesar_cipher(cipher_text)

"""
6. Encrypt and decrypt the string using Atbash cipher 
"""
def atbash_cipher(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    reversed_alphabet = alphabet[::-1] 
    cipher_map = dict(zip(alphabet, reversed_alphabet))
    cipher_map.update(dict(zip(alphabet.upper(), reversed_alphabet.upper())))

    result = ''.join(cipher_map.get(char, char) for char in text)
    return result

text_to_encode = input("Enter the Plaintext to encode and decode using atbash:")
encoded_text = atbash_cipher(text_to_encode)
print("Encoded:", encoded_text)

decoded_text = atbash_cipher(encoded_text)
print("Decoded:", decoded_text)

"""
7. Encrypt and decrypt using Affine cipher 
        add validation
"""
import math

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def affine_encrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            x = ord(char) - start
            encrypted_char = chr((a * x + b) % 26 + start)
            result.append(encrypted_char)
        else:
            result.append(char)
    return ''.join(result)

def affine_decrypt(text, a, b):
    if math.gcd(a, 26) != 1:
        raise ValueError("Key 'a' must be coprime with 26.")
    
    a_inv = mod_inverse(a, 26)
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            y = ord(char) - start
            decrypted_char = chr((a_inv * (y - b)) % 26 + start)
            result.append(decrypted_char)
        else:
            result.append(char)
    return ''.join(result)

a = 5
b = 8

plaintext = "Hello World"
encrypted_text = affine_encrypt(plaintext, a, b)
print(f"Encrypted Text: {encrypted_text}")

decrypted_text = affine_decrypt(encrypted_text, a, b)
print(f"Decrypted Text: {decrypted_text}")

try:
    invalid_a = 13
    affine_encrypt(plaintext, invalid_a, b)
except ValueError as e:
    print(f"Validation Error: {e}")

