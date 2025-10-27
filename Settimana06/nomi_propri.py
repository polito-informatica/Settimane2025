"""
Si scriva un programma che:
- acquisisca da tastiera un numero intero positivo N
- acquisisca da tastiera N frasi (una per riga) composte di più parole
- per ciascuna frase, identifichi i nomi propri in essa presenti 
  (un nome proprio ha la prima lettera maiuscola, e le altre minuscole)
- VARIANTE 1: si stampino tutti i nomi propri incontrati
- VARIANTE 2: si stampi solo il primo nome proprio incontrato su ciascuna riga
"""

# Xxxxx, Xx - si
# X, XXXXX, XxxxXxx - no

import string

N = int(input("Inserisci un numero: "))

#c = 0
#while c < N:
for c in range(N):
    FRASE = input("Inserisci una frase: ")
    #" AAAA Mario, oggi siamo andati AAAAAAA fare un girO con MaRia, Giovanni e Li"


    for i in range(len(FRASE)):

        if FRASE[i].isupper():

            if  i == 0 or FRASE[i-1].isspace() or FRASE[i-1] in string.punctuation:

                j = i + 1
                if j < len(FRASE) and FRASE[j].islower() and FRASE[j] not in string.punctuation:

                    while j < len(FRASE) and FRASE[j].islower():
                        j+=1
                    # qui i è l'indice dell'iniziale
                    # e j è l'indice della prima lettera dopo il nome

                    if j == len(FRASE) or FRASE[j].isspace() or FRASE[j] in string.punctuation:

                        nome_proprio = FRASE[i:j]
                        print(nome_proprio)

    #c+=1









