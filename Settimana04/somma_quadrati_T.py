# Dato un valore T inserito dall'utente, quanti quadrati dei numeri 
# interi bisogna sommare per fare sì che la somma sia > T ?


# 1 + 4+ 9+ 16+ 25 + 36 + ...

T = int(input("Inserisci il Totale: "))

somma = 0
i = 1
while somma <= T:
    quadrato = i * i
    somma = somma + quadrato  # accumulatore
    print(i, somma)

    i = i + 1


print(f'mi servivano {i-1} quadrati')