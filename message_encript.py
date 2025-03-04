import random
import string

chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#ENCRYPT

plain_text = input('Type a message:\n ')
cipher_text = ''

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f'original message: {plain_text}')
print(f'encrypted message: {cipher_text}')

#DECRYPT

cipher_text = input('Type a message:\n ')
plain_text = ''

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f'encrypted message: {cipher_text}')
print(f'original message: {plain_text}')