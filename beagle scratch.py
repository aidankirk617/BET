## Reverse Cipher
"""
user_input = input("Encrypt, or decrypt?: ")

if user_input.lower() == "encrypt":
    message = input("Enter String:")

    translated = ''

    i = len(message) - 1

    while i >= 0:

        translated = translated + message[i]

        i = i - 1


    print("After Encryption: " + translated)


if user_input.lower() == "decrypt":
    message = input("Enter String:")

    translated = ''

    i = len(message) + 1

    while i <= 0:

        translated = translated + message[i]

        i = i + 1


    print("After Decryption: " + translated)
"""

## Caeser Cipher
"""
user_input = input("Encrypt, or decrypt?: ")

if user_input.lower() == "encrypt":

  def encrypt(string, shift):

      cipher = ''
      for char in string:
          if char == ' ':
              cipher = cipher + char
          elif  char.isupper():
              cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
          else:
              cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

      return cipher

if user_input.lower() == "decrypt":

  def decrypt(string, shift):

      cipher = ''
      for char in string:
          if char == ' ':
              cipher = cipher + char
          elif  char.isupper():
              cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
          else:
              cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)

      return cipher

text = input("enter string: ")
s = int(input("enter shift number: "))
print("original string: ", text)
print("after encryption: ", encrypt(text, s))

text = input("enter code: ")
s = int(input("enter shift number: "))
print("original code: ", text)
print("after decryption: ", decrypt(text, s))
"""
## Transposition Cipher
"""
key = input("Index: ")
plaintext = input("String: ")

def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]

def encode(key, plaintext):

    order = {
        int(val): num for num, val in enumerate(key)
    }

    ciphertext = ''
    for index in sorted(order.keys()):
        for part in split_len(plaintext, len(key)):
            try:
                ciphertext += part[order[index]]
            except IndexError:
                continue

    return ciphertext

print(encode(key, plaintext))
"""
## Affine Cipher **GeeksforGeeks
"""
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modinv(a, m):
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m

def affine_encrypt(text, key):
    '''
    C = (a*P + b) % 26
    '''
    return ''.join([ chr((( key[0]*(ord(t) - ord('A')) + key[1] ) % 26)
                  + ord('A')) for t in text.upper().replace(' ', '') ])

def affine_decrypt(cipher, key):
    '''
    P = (a^-1 * (C - b)) % 26
    '''
    return ''.join([ chr((( modinv(key[0], 26)*(ord(c) - ord('A') - key[1]))
                    % 26) + ord('A')) for c in cipher ])

def main():
    text = input("String: ")
    key = [17, 20]

    affine_encrypted_text = affine_encrypt(text, key)

    print('Encrypted Text: {}'.format( affine_encrypted_text ))

    print('Decrypted Text: {}'.format
    ( affine_decrypt(affine_encrypted_text, key) ))


if __name__ == '__main__':
    main()
"""
## Substitution Cipher
"""
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz.,! '
key = 'nu.t!iyvxqfl,bcjrodhkaew spzgm'
plaintext = "Hey, this is really fun!"


def makeKey(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def encrypt(plaintext, key, alphabet):
    keyMap = dict(zip(alphabet, key))
    return ''.join(keyMap.get(c.lower(), c) for c in plaintext)

def decrypt(cipher, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c.lower(), c) for c in cipher)

cipher = encrypt(plaintext, key, alphabet)

print(plaintext)
print(cipher)
print(decrypt(cipher, key, alphabet))
"""