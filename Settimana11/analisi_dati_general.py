"""
Scrivere un programma Python che legga un file "dati_sensori.csv"
contenente dati ambientali (es. temperatura e umidità) in ordine temporale di
acquisizione in formato CSV e che supporti le seguenti funzionalità:

- PREPROCESSING DEI DATI: durante la lettura, gestire le eccezioni principali
(FileNotFoundError, IOError, ValueError),
  pre-processando i dati e scartando le righe con valori mancanti,
  celle vuote, colonne in eccesso/difetto o valori non numerici.
  Creare il file "qualità_dati.csv" che indichi quanti record validi
  e quanti scartati sono stati letti. Restituire la tabella contenente
  solo dati validi.

- RIORGANIZZAZIONE: organizzare i dati validi raggruppando
le misure per parametro in file separati (ad esempio "dati_temperatura.csv"
  e "dati_umidità.csv", se presenti nel file originale).

- RICHIESTA DATI: ottenere gli ultimi dati validi rilevati e il loro timestamp per sensore e tipologia di dato, supportando due modalità:
  una che restituisce solo l’ultimo valore, e un’altra che restituisce gli ultimi N valori, dove modalità ed eventuale N vengono forniti in input dall’utente.
  Gestire le eccezioni derivanti dall’inserimento di input non valido e dall’assenza di almeno N ultimi dati validi.

Versione GENERALIZZATA:
- Preprocessing con filtraggio righe invalide
- Riorganizzazione per QUALSIASI parametro (dati_<parametro>.csv)
- Richiesta ultimi dati per sensore e parametro (ultimo / ultimi N)
"""

import csv
import datetime 


def leggi_file(nome_file):

    try:
        with open(nome_file, "r") as in_f:
            csv_reader = csv.reader(in_f)
            tabella_dati_grezzi = list(csv_reader)
    except FileNotFoundError as e:
        print("File non trovato:\n", e)
        return None
    except IOError as ioe:
        print(ioe)
        return None
    
    return tabella_dati_grezzi


def preprocessa_dati(dati_grezzi):
        
    dati_validi = []
    conta_valide = 0
    conta_non_valide = 0

    if not dati_grezzi:
        return []

    for riga in dati_grezzi[1:]:

        valida = True  # assumo che la riga sia valida

        # --- CONTROLLO COLONNE ---
        if len(riga) != 4:
            valida = False

        # --- CONTROLLO CELLE VUOTE ---
        if valida:
            riga = [c.strip() for c in riga]
            if any(c == "" for c in riga):
                valida = False

        # --- CONTROLLO PARSING ---
        if valida:
            try:
                tempo = datetime.datetime.strptime(riga[0], "%Y-%m-%d %H:%M:%S")
                sensore = riga[1]
                parametro = riga[2]
                valore = float(riga[3])
            except ValueError:
                valida = False

        # --- DECISIONE FINALE ---
        if valida:
            dati_validi.append([
                tempo.strftime("%Y-%m-%d %H:%M:%S"),
                sensore,
                parametro,
                str(valore)
            ])
            conta_valide += 1
        else:
            conta_non_valide += 1

    # --- SCRITTURA FILE QUALITÀ ---
    with open("qualita_dati.csv", "w") as out_f:
        out_f.write("conta_valide,conta_non_valide\n")
        out_f.write(f"{conta_valide},{conta_non_valide}")

    # --- SCRITTURA FILE DATI VALIDATI ---
    with open("dati_validi.csv", "w") as out_f:
        csv_writer = csv.writer(out_f)
        csv_writer.writerow(dati_grezzi[0])  # header
        for r in dati_validi:
            csv_writer.writerow(r)

    return dati_validi


def riorganizza_dati(filename):
    """
    Versione generalizzata:
    - legge dati_validi.csv
    - individua tutti i parametri presenti
    - per ciascun parametro crea un file:
        dati_<parametro>.csv
    - restituisce la lista dei parametri trovati
    """

    try:
        with open(filename, "r") as in_f:
            csv_read = csv.reader(in_f)
            header = next(csv_read)   # salta header
            righe = list(csv_read)
    except FileNotFoundError as e:
        print(e)
        return None

    # Trovo l'elenco dei parametri distinti usando solo liste
    parametri = []
    for riga in righe:
        if len(riga) >= 3:
            p = riga[2]
            if p not in parametri:
                parametri.append(p)

    # Per ogni parametro creo il file corrispondente
    for parametro in parametri:
        nome_file = f"dati_{parametro}.csv"
        with open(nome_file, "w") as out_f:
            csv_writer = csv.writer(out_f)
            # se vuoi, puoi reinserire l'header qui:
            # csv_writer.writerow(header)
            for riga in righe:
                if len(riga) >= 3 and riga[2] == parametro:
                    csv_writer.writerow(riga)

    return parametri


def richiesta_dati(sensore, parametro):
    """
    Versione generalizzata:
    - parametro è una stringa come nel CSV (es. "temperature", "humidity", "CO2", ...)
    - usa il file dati_<parametro>.csv
    - chiede:
        1) ultimo valore
        2) ultimi N valori
    - nessun ordinamento: i dati sono già in ordine temporale nel file originale
    """

    righe = []

    # Nome del file associato al parametro
    filename = f"dati_{parametro}.csv"

    # Lettura del file
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)

            # qui NON c'è header, quindi non faccio next(reader)

            for riga in reader:
                if len(riga) >= 4 and riga[1] == sensore:
                    righe.append(riga)

    except FileNotFoundError as e:
        print("File mancante per il parametro richiesto:", e)
        return None

    if not righe:
        print(f"Nessun dato trovato per sensore '{sensore}' e parametro '{parametro}'.")
        return None

    # Scelta modalità
    while True:
        scelta = input("Vuoi l'ultimo valore (1) o gli ultimi N valori (2)? ").strip()

        if scelta == "1":
            # Ultimo valore disponibile: l’ultimo nel file
            ultima = righe[-1]
            # timestamp = ultima[0], valore = ultima[3]
            return ultima[0], ultima[3]

        elif scelta == "2":
            ok = False
            while not ok:
                try:
                    n = int(input("Quanti valori vuoi (N)? ").strip())
                    if n <= 0:
                        print("N deve essere un numero positivo.")                    
                    elif n > len(righe):
                        print(f"Errore: richiesti {n} valori, ma disponibili solo {len(righe)}.")
                    else:
                        ok = True
                        # Ultimi N valori: prendo dalla fine
                        return righe[-n:]
                except ValueError:
                    print("Inserisci un numero intero valido.")
        else:
            print("Scelta non valida. Inserisci '1' o '2'.")


if __name__ == "__main__":
    
    tabella_dati_grezzi = leggi_file("dati_sensori.csv")
    tabella_dati_validi = preprocessa_dati(tabella_dati_grezzi)
    print("Dati validi letti:", len(tabella_dati_validi))

    parametri = riorganizza_dati("dati_validi.csv")
    print("Parametri trovati:", parametri)

    # Esempio di richiesta:
    # sensore S1, parametro "temperature" (come scritto nel CSV)
    print(richiesta_dati("S1", "temperature"))
