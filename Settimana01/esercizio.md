# Esercizio

Quali sono i nomi più frequenti in questa aula?

# Analisi

Definiamo QUANTI nomi vogliamo elencare (es. 5)

Cosa facciamo in caso di nomi a pari merito?
es. ne scelgo uno qualunque
es. scelgo il primo in ordine alfabetico
es. li stampo comunque tutti (sforando il numero di nomi previsti)

"Ugo""
"Pier Paolo"
Nel caso di nomi composti, questi si considerano come un nome unico.
(oppure: questi di dividono nei nomi componenti, che vengono calcolati
separatamente)

Il formato di stampa deve riportare i nomi più frequenti,
in ordine di frequenza decrescente,
ciascuno con a fianco il valore della propria frequenza assoluta.
(in caso di parità di frequenza, l'ordine non importa)

Non ho idea di chi  sia presente in quest'aula...

Possiamo invece chiederci:
Qual è il nome più frequente tra gli iscritti al corso?

(l'elenco è disponibile in file che si può scaricare)

Qual è il nome più frequente all'interno del file?
(i nomi sono sulla terza colonna)

# Progettazione / Design

(1)
Prendo una per volta le righe del file (saltando quelle che contengono
        un nome già visto)
    Prendo il nome di quella riga
    Vado a contare quante volte tale nome compare nelle altre righe
    Mi memorizzo quel nome + il conteggio

E 10
A 14
Z 6
W 2
...

(2)
    Metto in ordine questa "tabella" memorizzata, secondo i valori
    numerici decrescenti della seconda colonna.

    Prendo le prime 5 righe della tabella ordinata e le stampo.

Alternativa ad (1)

Prendo una riga del file per volta
    Prendo il nome di quella riga
    Nella tabella delle frequenze, esiste già questo nome?
    Se sì, aumenta di 1 la sua frequenza
    Se no, aggiungila mettendo a 1 la frequenza

DAVIDE 2
SAMUELE 1
GIANLUCA 1

Alternativa bis a (1)

Leggo tutte le righe
    Prendo tutti i nomi
    Metto in nomi in ordine alfabetico
    Per ciascun gruppo di nomi consecutivi uguali, conto quanti sono