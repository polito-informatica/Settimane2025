nome = input("Inserisci il nome: ")
print(nome)

numero1 = input("Inserisci il numero: ")

# funziona con stringhe che rappresentano float e anche int
numero1 = float(numero1)
print(numero1)

# funziona con stringhe che rappresentano int ma non float
numero2 = int(input("Inserisci il numero: "))
print(numero2)

# se non faccio le conversioni a valori numerici, qui mi ritrovo 
# con una concatenazione tra stringhe
somma = numero1 + numero2
print(somma)

# se non inserisco il prompt, per l'utente il dato da inserire
# resta un mistero
mistero = input()
print(mistero)

# diversi modi di stampare a terminale espressioni

print("Il primo numero inserito è stato", numero1)

print(f"Il primo numero inserito è stato {numero1:.7f}")

print(f"Visualizza questo numero: {7/4:.1f}")

print(f"Visualizza questo numero: {230:10.1f}")