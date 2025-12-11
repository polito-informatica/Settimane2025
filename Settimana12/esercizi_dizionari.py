# Dizionario dei colori preferiti.
# NOTA: in un dizionario le chiavi devono essere uniche.
# Qui "Adam" compare due volte: l'ultimo valore ("Blu") sovrascrive il precedente.
colori_preferiti = {
    "Romeo": "Rosso",
    "Adam": "Verde", # "Verde" viene perso perché sovrascritto
    "Adam": "Blu"   
}

# Stampa delle coppie chiave-valore
for chiave, valore in colori_preferiti.items():
    print(chiave, valore)

print()

# Stampa delle chiavi
print(colori_preferiti.keys())

print()

# Stampa dei valori
print(colori_preferiti.values())


# Liste di nomi e colori per ricostruire il dizionario
nomi = ["Anna", "Maria", "Giacomo"]
colori = ["Blu", "Verde", "Ramato"]

# Svuota il dizionario
colori_preferiti.clear()

# Ricostruisce il dizionario associando ad ogni nome il colore corrispondente
for i, nome in enumerate(nomi):
    colori_preferiti[nome] = colori[i]

# Stampa dei valori ordinati alfabeticamente per chiave
for chiave in sorted(colori_preferiti):
    print(colori_preferiti[chiave])

# Stampa finale di tutte le coppie chiave-valore
for k, v in colori_preferiti.items():
    print(k, v)