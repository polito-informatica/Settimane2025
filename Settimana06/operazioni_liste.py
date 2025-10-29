
lista = []

lista.append(1)
lista.append("ciao")
lista.append(12.9)
lista.append("ciao")
#lista.append([1, 2, 3])

#el = lista[3][0]
#print(el)

lista.insert(2, "nuovo")
print(lista)

presenza_ciao = "ciao" in lista

if presenza_ciao:
    indice_ciao = lista.index("ciao")
    print(indice_ciao)

#indice_buongiorno = lista.index("buongiorno")

print(lista)
lista.pop()
print(lista)
lista.pop(0)
print(lista)

lista2 = ["a", "b", "c"]

concatenata = lista + lista2
print(concatenata)

replicata = lista2 * 3
print(replicata)

print("ab"*3)

lista_numeri = [1,10,2,70,3,4]
lista_parole = ["cane", "zio", "sole"]

print(sum(lista_numeri))

print(min(lista_numeri))
print(min(lista_parole))

print(lista_numeri)
lista_numeri.sort()
print(lista_numeri)

print(lista_parole)
lista_ordinata = sorted(lista_parole)
print(lista_parole)
print(lista_ordinata)

print()
print()
print()

nomi = ["Marco", "Gianna", "Valeria", "Stefano", "Federico", "Valeria"]

for (i, nome) in enumerate(nomi):
    #if nomi.index(nome) == len(nomi)-1:
    if i == len(nomi)-1:
        print(f"{nome}")
    else:
        print(f"{nome}, ", end="")



