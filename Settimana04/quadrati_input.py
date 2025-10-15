# stampa i quadrati di tutti i numeri che l'utente inserisce da tastiera
# finché l'utente non inserisce il valore zero
'''
numero = -1
# numero = ""

while numero != 0:
    numero = int(input("Numero: "))
    if numero != 0:
        quadrato = numero * numero
        print(numero, quadrato)

print("fine")
'''

# DRY Don't Repeat Yourself

'''
numero = int(input("Numero: "))

while numero != 0:
    
    quadrato = numero * numero
    print(numero, quadrato)

    numero = int(input("Numero: "))

print("fine")
'''

# stampa i quadrati di tutti i numeri che l'utente inserisce da tastiera
# finché l'utente non inserisce il valore "*"


risposta = input("Numero: ")

while risposta != "*":
    numero = int(risposta)
    quadrato = numero * numero
    print(numero, quadrato)

    risposta = input("Numero: ")

print("fine")





