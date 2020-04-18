
## Reverse Cipher
"""
message = input("Enter String: ")
toString = ''
i = len(message) - 1

while i >= 0:
   toString = toString + message[i]
   i = i - 1
print("\noriginal code: ", message)
print("The cipher text is : ", toString)
"""


## Caeser Cipher
"""
def encrypt(string, shift):
    text = input("enter string: ")
    s = int(input("enter shift number: "))
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)

    return cipher
    print("original string: ", text)
    print("after encryption: ", encrypt(text, s))

def decrypt(string, shift):
    text = input("enter code: ")
    s = int(input("enter shift number: "))
    cipher = ''
    for char in string:
        if char == ' ':
            cipher = cipher + char
        elif  char.isupper():
            cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)

    return cipher
    print("original code: ", text)
    print("after decryption: ", decrypt(text, s))
"""

## Transposition Cipher
"""
def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]
def encode(key, plaintext):
    order = {
        int(val): num for num, val in enumerate(key)
    }
ciphertext = ''

for index in sorted(order.keys()):
    for part in split_len(plaintext, len(key)):
      try:ciphertext += part[order[index]]
        except IndexError:
            continue
    return ciphertext
print(encode('3214', 'HELLO'))
"""
## Affine Cipher
"""
class Affine(object):
   DIE = 128
   KEY = (7, 3, 55)

   def __init__(self):
      pass

   def encryptChar(self, char):
      K1, K2, kI = self.KEY
      return chr((K1 * ord(char) + K2) % self.DIE)

   def encrypt(self, string):
      return "".join(map(self.encryptChar, string))

   def decryptChar(self, char):
      K1, K2, KI = self.KEY
      return chr(KI * (ord(char) - K2) % self.DIE)

   def decrypt(self, string):
      return "".join(map(self.decryptChar, string))
      affine = Affine()

print(Affine.encrypt('Affine Cipher'))
print(Affine.decrypt('*18?FMT'))
"""

## Multiplicative Cipher
"""
def unshift(key, ch):
   offset = ord(ch) - ASC_A
   return chr(((key[0] * (offset + key[1])) % WIDTH) + ASC_A)
"""
## Substitution Cipher
"""
import random, sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def main():
   message = ''
   if len(sys.argv) > 1:
      with open(sys.argv[1], 'r') as f:
         message = f.read()
   else:
      message = raw_input("Enter your message: ")
   mode = raw_input("E for Encrypt, D for Decrypt: ")
   key = ''

   while checkKey(key) is False:
      key = raw_input("Enter 26 ALPHA key (leave blank for random key): ")
      if key == '':
         key = getRandomKey()
      if checkKey(key) is False:
        print('There is an error in the key or symbol set.')
   translated = translateMessage(message, key, mode)
   print('Using key: %s' % (key))

   if len(sys.argv) > 1:
      fileOut = 'enc.' + sys.argv[1]
      with open(fileOut, 'w') as f:
         f.write(translated)
      print('Success! File written to: %s' % (fileOut))
   else: print('Result: ' + translated)

# Store the key into list, sort it, convert back, compare to alphabet.
def checkKey(key):
   keyString = ''.join(sorted(list(key)))
   return keyString == LETTERS
def translateMessage(message, key, mode):
   translated = ''
   charsA = LETTERS
   charsB = key

   # If decrypt mode is detected, swap A and B
   if mode == 'D':
      charsA, charsB = charsB, charsA
   for symbol in message:
      if symbol.upper() in charsA:
         symIndex = charsA.find(symbol.upper())
         if symbol.isupper():
            translated += charsB[symIndex].upper()
         else:
            translated += charsB[symIndex].lower()
                else:
                    translated += symbol
         return translated

def getRandomKey():
   randomList = list(LETTERS)
   random.shuffle(randomList)
   return ''.join(randomList)
if __name__ == '__main__':
   main()
"""
## RSA Cipher
"""
def p_and_q(n):
   data = []
   for i in range(2, n):
      if n % i == 0:
         data.append(i)
   return tuple(data)

def euler(p, q):
   return (p - 1) * (q - 1)

def private_index(e, euler_v):
   for i in range(2, euler_v):
      if i * e % euler_v == 1:
         return i

def decipher(d, n, c):
   return c ** d % n
   def main():
      e = int(input("input e: "))
      n = int(input("input n: "))
      c = int(input("input c: "))

      # t = 123
      # private key = (103, 143)
      p_and_q_v = p_and_q(n)
      # print("[p_and_q]: ", p_and_q_v)
      euler_v = euler(p_and_q_v[0], p_and_q_v[1])

      # print("[euler]: ", euler_v)
      d = private_index(e, euler_v)
      plain = decipher(d, n, c)
      print("plain: ", plain)

if __name__ == "__main__":
   main()
"""