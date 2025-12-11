def apri_file(filename):
    """
    Apre un file di testo e restituisce la prima riga divisa in parole.
    """

    try:
        # "with" gestisce automaticamente l'apertura e la chiusura del file
        with open(filename, "r", encoding="UTF-8") as f:
            testo = f.readline()      # legge solo la prima riga
            parole = testo.split()    # divide la stringa in base agli spazi
            return parole

    except FileNotFoundError as e:
        print("Errore: il file non è stato trovato.")
        print(e)
        return []   # importante restituire una lista vuota per evitare crash


def conta_parole(lista_parole):
    """
    Conta quante volte ogni parola compare nella lista.
    Restituisce un dizionario {parola: conteggio}.
    """

    mappa_conteggio = {}

    for parola in lista_parole:
        # Se la parola è già presente, incrementa il conteggio
        if parola in mappa_conteggio:
            mappa_conteggio[parola] += 1
        else:
            # altrimenti la aggiunge con conteggio = 1
            mappa_conteggio[parola] = 1
    
    return mappa_conteggio



parole = apri_file("testo_libero.txt")
mappa = conta_parole(parole)
print(mappa)
