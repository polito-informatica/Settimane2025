PAROLA_SEGRETA = input("Inserisci la parola segreta: ")

#parola_inserita = input("Indovina la parola: ")

#parola_inserita = ""
#while parola_inserita != PAROLA_SEGRETA:

continua = True

while continua:
    
    parola_inserita = input("Indovina la parola: ")

    if parola_inserita == PAROLA_SEGRETA:
        print("Indovinato!")
        continua = False
    

    if len(parola_inserita) == len(PAROLA_SEGRETA):
        i = 0
        while i < len(parola_inserita):
            lettera = parola_inserita[i]
            if lettera == PAROLA_SEGRETA[i]:
                print(lettera, end="")
            else:
                print("_", end="")
            i+=1
    else:
        i = 0
        while i < len(parola_inserita):
            if parola_inserita[i] in PAROLA_SEGRETA:
                print(parola_inserita[i], "presente")
            else: 
                print(parola_inserita[i], "assente")
            i+=1
    print("Sarai più fortunat*")




print("Indovinato!")


"""
if parola_inserita == PAROLA_SEGRETA:
    print("Indovinato!")
else:
    print("Sarai più fortunat*")
"""
