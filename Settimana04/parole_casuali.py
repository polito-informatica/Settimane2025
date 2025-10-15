
# Stampare 10 parole casuali di lunghezza compresa tra 5 e 10 lettere
# ciascuna
# suggerimento: random.random, ord, chr

import random

# si scompone in:
# a) ripeti 10 volte un'operazione
# b) costruisci una stringa più o meno random

volte = 0

while volte < 10:

    # b1. costruisci una stringa di lunghezza casuale

    lunghezza = random.randint(5, 10)

    # i = 0
    # s = ""
    # while i<lunghezza:
    #     s = s + "*"
    #     i = i + 1

    s = ""
    while len(s)<lunghezza:

        # b2. scegli un singola lettera, casualmente
        # b2a. scelgo un numero tra 1 e 26 o tra 0 e 25
        # b2b. scelgo la lettera dell'alfabeto in tale posizione

        alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        posiz_lettera = random.randint(1, len(alfabeto))
        lettera = alfabeto[posiz_lettera-1]

        s = s + lettera

    print(s)

    volte = volte + 1

# import string
# alfabeto = string.ascii_uppercase

