def convert(list): 
    """Merge list of integers to one integer """ 
    # Converting integer list to string list 
    s = [str(i) for i in list] 
    # Join list items using join() 
    res = int("".join(s)) 
      
    return(res)

def encode(message):
    """ Encode message into ascii array"""
    chars = []
    for c in message:
        
        chars.append(ord(c))
    return chars



one = encode("hello how are you my friend")
two = convert(one)
print(two)

def decode(message):
    message = str(message)
    decoded = []
    slider = 3
    numList = [int(message[i:i+slider]) for i in range(0, len(message), slider)]
   
    
    for i in range(len(numList)):
        decoded.append(chr(numList[i]))

    decoded = ''.join(decoded)

    return decoded
print(decode(two))
message = 1511

# 2 prime mumbers

p = 47
q = 61
n = p*q
phi = (p-1)*(q-1)

e = 7


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# calculate our exponent
d = modinv(e, phi)

# Encrypt our message
def encrypt(message, e, n):
    """ Return encrypted message cipher"""
    return (message**e) % n


cipher = encrypt(message, e, n)
print(cipher)


# decrypt our message
def decrypt(cipher, d, n):
    """ Return decrypted message cipher"""
    return (cipher**d) % n



print(decrypt(cipher, d, n))