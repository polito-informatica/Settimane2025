nomi = [ "Pippo", "Pluto", "Paperino", "Nonna Papera" ]

altri = nomi  # alias

altri = list(nomi)  # copia

altri = nomi[:]  # copia



nomi[1:3]  # il risultato a sua volta è una lista
nomi[1]    # il risultato è un singolo elemento  -> "Pluto"
nomi[1:2]  # -> [ "Pluto" ]






# quali sono le lettere iniziali dei nomi di questa lista?

for i in range(len(nomi)):
    nome = nomi[i]
    iniziale = nome[0]
    print(iniziale)

len(nomi[0])

for i in range(len(nomi)):
    print(nomi[i][0])

for nome in nomi:
    print(nome[0])



numeri = [ 36, 88, 712 ]

str(numeri[i])[0]

