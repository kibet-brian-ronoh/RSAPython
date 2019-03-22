import math

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


d = modinv(e, phi)

# Encrypt our message
cypher = (message**e) % n
print(cypher)


# decrypt

origMessage = (cypher**d) % n
print(origMessage)