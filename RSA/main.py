import numpy as np
from math import sqrt
import math
from random import randrange, getrandbits
import json
import os


p = 0
q = 0
defult_e = 65537
text = ''
Carr = []

def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True


def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p


def search_n(p, q):
    n = p * q
    return n


def euclid_alg(e, fi):
    u = (e, 1)
    v = (fi, 0)
    while v[0] != 0:
        q = u[0] // v[0]
        t = (u[0] % v[0], u[1] - q * v[1])
        u = v
        v = t
    if u[0] != 1:
        return 0
    return u[1] % fi


def search_fi(p, q):
    fi = (p - 1) * (q - 1)
    return fi


def search_d(p, q):
    fi = search_fi(p, q)
    e = defult_e
    d = euclid_alg(e, fi)
    return d


def generate_prime_number(length=8):
    global p, q, n, fi, d, e
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    q = 4
    # keep generating while the primality test fail
    while not is_prime(p, 10):
        p = generate_prime_candidate(length)
    while not is_prime(q, 10):
        q = generate_prime_candidate(length)
    n = search_n(p, q)
    fi = search_fi(p, q)
    d = search_d(p, q)
    e = defult_e


def input_p_q():
    global p, q, n, fi, d, e
    p = input("p: ")
    q = input("q: ")
    p = int(p)
    q = int(q)
    n = search_n(p, q)
    fi = search_fi(p, q)
    d = search_d(p, q)
    e = defult_e


def encode(text, e, n):
    Marr = []
    global Carr
    # представление текста в виде последовательности кодов символов
    for i in range(0, len(text)):
        Marr.append(ord(text[i]) % n)
    Carr = []
    # шифрование последовательности кодов символов
    for i in range(0, len(Marr)):
        Carr.append((Marr[i] ** e) % n)
    print(*Carr)
    return Carr


def decode(Carr, d, n):
    marr = []
    # дешифровка последовательности кодов символов
    for i in range(0, len(Carr)):
        marr.append((int(Carr[i]) ** int(d)) % int(n))
    # перевод дешиврованной последовательности обратно в текст
    DecText = []

    for i in range(0, len(marr)):
        DecText.append(chr(marr[i]))
    fin = ''
    print(fin.join(DecText))



def Menu(value):
    Arr=[]
    global text
    match (value):
        case 1:
            print("1. Enter the key yourself")
            print("2. Generate key")
            vallue = input("Select:  ")
            vallue = int(vallue)
            match vallue:
                case 1:
                    input_p_q()
                case 2:
                    generate_prime_number()
                case _:
                    default()
            print(f'pub: [{e} {n}] , priv: [{d} {n}]')
            text = input("Enter a message to encode: ")
            encode(text, e, n)
            print("Decode this message?")
            print("1. yes")
            print("2. no")
            vallue_3 = input('Select: ')
            if int(vallue_3) == 1:
                decode(Carr, d, n)
        case 2:
            Arr = list(map(int, input('Enter a message to decode: ').split()))
            priv_k = list(map(int, input("Enter priv key: ").split()))
            decode(Arr, priv_k[0], priv_k[1])




def start():
    try:
        print()
        print("Welcome to RSA_encoder! To select please specify 1 or 2:  ")
        print("1. Encode")
        print("2. Decode")
        value = input("Select:  ")
        Menu(int(value))
    except ValueError:
        print('Wrong input!')

    print()
    print('Restart?')
    print("1. yes")
    print("2. no")
    rst = input()
    rst=int(rst)
    match rst:
        case 1:
            print()
            start()
start()