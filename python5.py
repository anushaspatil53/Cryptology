def mod_inverse(a, m):
    """Find the modular inverse of a under modulo m."""
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_decrypt(ciphertext, a, b):
    """Decrypt the ciphertext using the Affine cipher with given keys."""
    m = 26  # Size of the alphabet
    a_inv = mod_inverse(a, m)
    if a_inv is None:
        return ""
    
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            start = ord('a') if char.islower() else ord('A')
            char_val = ord(char) - start
            decrypted_char_val = (a_inv * (char_val - b)) % m
            decrypted_char = chr(decrypted_char_val + start)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)

def brute_force_affine_keys(plaintext_pair, ciphertext_pair, ciphertext):
    p1, p2 = plaintext_pair
    c1, c2 = ciphertext_pair
    m = 26
    results = []
    
    for a in range(1, m):
        if mod_inverse(a, m) is None:
            continue
        for b in range(m):
            # Test if (a, b) pair encrypts plaintext to ciphertext
            if (a * p1 + b) % m == c1 and (a * p2 + b) % m == c2:
                decrypted_text = affine_decrypt(ciphertext, a, b)
                results.append((a, b, decrypted_text))
    
    return results

# Given values
plaintext_pair = (ord('a') - ord('a'), ord('b') - ord('a'))  # 'a' -> 0, 'b' -> 1
ciphertext_pair = (ord('G') - ord('A'), ord('L') - ord('A'))  # 'G' -> 6, 'L' -> 11
ciphertext = "XPALASXYFGFUKPXUSOGEUTKCDGFXANMGNVS"

# Perform brute force attack
results = brute_force_affine_keys(plaintext_pair, ciphertext_pair, ciphertext)

# Output results
for a, b, decrypted_text in results:
    print(f"Keys found: a = {a}, b = {b}")
    print(f"Decrypted text: {decrypted_text}")

