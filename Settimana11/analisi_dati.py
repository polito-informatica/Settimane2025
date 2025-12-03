"""
Scrivere un programma Python che legga un file "dati_sensori.csv"
contenente dati ambientali (es. temperatura e umidità) in ordine temporale di
acquisizione in formato CSV e che supporti le seguenti funzionalità:

- PREPROCESSING DEI DATI: durante la lettura, gestire le eccezioni principali (FileNotFoundError, IOError, ValueError),
  pre-processando i dati e scartando le righe con valori mancanti, celle vuote, colonne in eccesso/difetto o valori non numerici.
  Creare il file "qualità_dati.csv" che indichi quanti record validi e quanti scartati sono stati letti. Restituire la tabella contenente
  solo dati validi.

- RIORGANIZZAZIONE: organizzare i dati validi raggruppando le misure per parametro in file separati (ad esempio "dati_temperatura.csv"
  e "dati_umidità.csv", se presenti nel file originale).

- RICHIESTA DATI: ottenere gli ultimi dati validi rilevati e il loro timestamp per sensore e tipologia di dato, supportando due modalità:
  una che restituisce solo l’ultimo valore, e un’altra che restituisce gli ultimi N valori, dove modalità ed eventuale N vengono forniti in input dall’utente.
  Gestire le eccezioni derivanti dall’inserimento di input non valido e dall’assenza di almeno N ultimi dati validi.

- GENERALIZZAZIONE: modificare il programma in modo che non gestisca solamente temperatura e umidità, ma qualsiasi parametro riportato
  nel file "dati_sensori.csv", a patto che rispetti la stessa formattazione.
"""
