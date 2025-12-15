"""

1. leggi il file con i brani e memorizzalo
in una lista di dizionari (? proviamo ?)

    tracce = [
        {
            'id': 1733,
            'composer': 'Schubert',
            'composition': 'Piano Sonata in A major'
            'movement': '2. Andantino',
            'ensemble': 'Solo Piano',
            'catalog_name': 'D959',
            'seconds': 546
        },
        {
           ....
        }
    ]

2. apro il file con i comandi
Per ogni riga dal file:
   se è c:... cerca per autore
   se è s:... cerca per formazione musicale

"""

import csv  # se uso DictReader serve il modulo csv


def main():

    # tracce = leggi_tracce("musicnet.csv")  ## versione base con la lettura "manuale"

    tracce = leggi_tracce_dictreader("musicnet.csv")  ## alternativa usando dictreader

    print(f"Ho letto {len(tracce)} tracce")

    with open("richieste.txt", "r", encoding="utf-8") as f:
        for riga in f:
            campi = riga.rstrip("\n").split(":")
            comando = campi[0]
            argomento = campi[1]

            if comando == "c":
                print(f"Cerca l'autore {argomento}")
                cerca_per_autore(argomento, tracce)
            elif comando == "s":
                print(f"Cerca la formazione musicale {argomento}")
                cerca_per_formazione(argomento, tracce)
            else:
                print("Comando non riconosciuto")


def leggi_tracce(nome_file):
    """
    Legge dal file CSV le tracce musicali e costruisce una lista di dizionari.

    :param nome_file: Nome del file (stringa)
    """
    tracce = []

    with open(nome_file, "r", encoding="utf-8") as f:
        f.readline()  # salta la prima riga
        for riga in f:
            campi = riga.rstrip("\n").split(",")
            traccia = {
                "id": int(campi[0]),
                "composer": campi[1],
                "composition": campi[2],
                "movement": campi[3],
                "ensemble": campi[4],
                "catalog_name": campi[5],
                "seconds": int(campi[6]),
            }
            tracce.append(traccia)

    return tracce


def leggi_tracce_dictreader(nome_file):
    tracce = []
    with open(nome_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for record in reader:
            # ad ogni riga del file viene restituito direttamente un dizionario (record)
            # le chiavi del dizionario vengono prese dalla prima riga del file

            # converto in int i campi numerici
            record["id"] = int(record["id"])
            record["seconds"] = int(record["seconds"])

            tracce.append(record)
    return tracce


def cerca_per_autore(autore, tracce):
    mie_tracce = []  # tracce di questo autore
    opere = set()
    for traccia in tracce:
        if traccia["composer"] == autore:
            mie_tracce.append(traccia)
            opere.add(traccia["catalog_name"])
    # print(mie_tracce)
    # print(opere)
    if len(mie_tracce) == 0:
        print("Compositore non presente in catalogo")

    for opera in opere:
        # cerca i movimenti di questa opera
        movimenti = []
        durata = 0
        for traccia in mie_tracce:
            if traccia["catalog_name"] == opera:
                movimenti.append(traccia)
                durata = durata + traccia["seconds"]

        print(f'- {opera}: {movimenti[0]["composition"]}, {durata} secondi')
        print(f"  {len(movimenti)} movimenti, in media {durata/len(movimenti)} secondi")


def cerca_per_formazione(formazione, tracce):
    mie_tracce = []
    opere = set()
    for traccia in tracce:
        if traccia["ensemble"] == formazione:
            mie_tracce.append(traccia)
            opere.add(traccia["catalog_name"])

    if len(mie_tracce) == 0:
        print("Formazione musicale non presente in catalogo")

    for opera in opere:
        autore = ""
        pos = 0
        while autore == "" and pos < len(mie_tracce):
            if mie_tracce[pos]["catalog_name"] == opera:
                autore = mie_tracce[pos]["composer"]
            pos = pos + 1
        print(f"- {autore}, opera {opera}")


main()

# t = leggi_tracce('musicnet.csv')
# print(t)
