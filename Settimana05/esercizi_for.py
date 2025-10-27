
import random


nome = "Annachiara"

for carattere in nome:
    print(carattere, end="")

print()

# equivale a...
i=0
while i < len(nome):
    print(nome[i])
    i = i +1 

print()

for indice in range(10):
    print(indice)

# equivale a...
i = 0
while i <10:
    print(i)
    i = i + 1

print()

n = int(input("Inserisci n: "))
while n < 10:
    print(n)
    n = int(input("Inserisci n: "))

n = random.randint(0,100)
while n < 50:
    print(n)
    n = random.randint(0,100)

# equivale a...
# nulla col for, perché non conoscendo il numero di iterazioni
# è corretto usare il while

# iterare su indice e valore


for (i, lettera) in enumerate(nome):
    print(i, lettera)

