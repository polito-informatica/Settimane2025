"""
Gestire la lista d'attesa per un locale.
Le persone in lista sono identificate con il proprio nome, e non ci sono omonimi. 
Il programma prende in input un'operazione che inserisce l'utente, 
la quale in questo caso è la persona che gestisce gli ingressi all'evento. 
Le operazioni da gestire sono le seguenti (i nomi delle persone sono a titolo esemplificativo):

P mina -> restituisci la Posizione di mina (se non è presente, segnalalo)
A pippo -> Aggiungi in coda pippo (se è già presente, segnalalo)
R gina -> Rimuovi dalla coda gina (se non è presente, segnalalo)
I john -> Inserisci in testa john (se è già presente, segnalalo)

Dopo ogni iterazione, il programma restituisce in output la lista d'attesa nel suo stato corrente, con il formato:

1 john
2 gale
3 iram
4 melany
5 pippo

Il programma termina quano viene inserita in input la stringa vuota ("").

"""