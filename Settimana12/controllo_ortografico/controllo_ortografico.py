import string

FILE_STORIA = 'story.txt'
FILE_DIZIONARIO = 'words.txt'

def main():
    dizionario = leggi_dizionario(FILE_DIZIONARIO)
    parole_storia = leggi_parole_storia(FILE_STORIA)

    parole_errate = parole_storia.difference(dizionario)

    print(parole_errate)


def leggi_dizionario(nome_file):
    elenco = set()
    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            elenco.add(riga.rstrip('\n').lower())
    return elenco

def leggi_parole_storia(nome_file):
    elenco_parole = set()

    with open(nome_file, 'r', encoding='utf-8') as f:
        for riga in f:
            parole = riga.rstrip('\n').split()
            for parola in parole:
                # normalizza la parola
                parola = parola.lower()
                parola = parola.strip(string.punctuation)

                elenco_parole.add(parola)
    return elenco_parole


main()