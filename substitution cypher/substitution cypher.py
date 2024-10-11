# substitution cypher

import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + " "
chars = list(chars)

key = chars.copy()
random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key:   {key}")

# encrypt
plane_text = input("Enter message to encrypt: ")
cipher_text = ""

for char in plane_text:
    index = chars.index(char)
    cipher_text += key[index]



print(f"Original message:  {plane_text}")
print(f"Encrypted message: {cipher_text}")
print()

# decrypt
cipher_text = input("Enter message to encrypt: ")
plane_text = ""

for char in cipher_text:
    index = key.index(char)
    plane_text += chars[index]

print(f"Encrypted message: {cipher_text}")
print(f"Decrypted message: {plane_text}")