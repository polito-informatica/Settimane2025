import string

NOME_FILE = 'story.txt'

elenco_parole = set()

with open(NOME_FILE, 'r', encoding='utf-8') as f:
    for riga in f:
        parole = riga.rstrip('\n').split()
        for parola in parole:
            # normalizza la parola
            parola = parola.lower()
            parola = parola.strip(string.punctuation)

            elenco_parole.add(parola)

print("Ci sono ", len(elenco_parole), " parole uniche")