# N = 12
# N = int(input("Inserisci il numero da indovinare: "))

import random

N = random.randint(0, 10)

print("Il numero generato randomicamente è ", N)

tentativi = 0

numero_inserito = int(input("Indovina il numero: "))
tentativi += 1

while numero_inserito != N and tentativi < 4:
    
    numero_inserito = int(input("Indovina il numero: "))
    print(numero_inserito)
    tentativi += 1


