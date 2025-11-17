'''
counts = [
    [ 0, 3, 0 ],
    [ 0, 0, 1 ],
    [ 0, 0, 1 ],
    [ 1, 0, 0 ],
    [ 0, 0, 1 ],
    [ 3, 1, 1 ],
    [ 0, 1, 0 ],
    [ 1, 0, 1 ]
    ]
print(counts)
print(counts[0][0])

medaglia_russia=counts[5][1]

for nazioni in counts:
    for tipo in nazioni:
        print(tipo)

# Soperazioni sulla riga 
med_italia=sum(counts[1])
print(med_italia)

# Operazioni sulla colonna
for tipo in range(3):
    med=0
    for riga in range(len(counts)):
        med= med +counts[riga][tipo]
    print(med)

counts[18][2]=5
'''

'''
C= 3 # Numero di colonne = tipo di medaglie
R= 4 # Numero di righe = Nazioni

#######################################################################
# Metodo riempimento tabella A:
# inizializzo e poi riempio con i valori veri
######################################################################

tabella=[]
riga= [0]*C
print(riga)
for i in range(R):
    tabella.append(list(riga)) # se non uso list cosa succede?
print(tabella)

# Se non uso list a linea 48 cosa si ottienen da queste due espressioni?
# tabella[5]=[1,2,3] 
# tabella[]

for r in range(R):
    for c in range(C):
        valore=int(input(f'Numero di medaglie in pos {r}{c}: '))
        tabella[r][c]=valore

for righe in tabella:
    print(righe)


#######################################################################
# Metodo riempimento tabella B:
# creo prima la riga appendendo elementi e poi appendo le righe
######################################################################
tabellaMed=[]

for r in range(R):
    nazione=[]
    tabellaMed.append(nazione)
    for c in range(C):
        valore=int(input(f'Numero di medaglie in pos {r}{c}: '))
        nazione.append(valore)
'''
#############################################################################
#                          CAMPO FIORITO
#############################################################################
"""
Consideriamo il gioco del Campo Fiorito,
in cui in una griglia quadrata di NxN caselle di prato sono presenti M fiori.

🐝 Chi gioca deve scoprire tutte le caselle che contengono fiori,
evitando di perdere tempo esplorando quelle che invece contengono solo una zolla d'erba.

Il programma deve innanzitutto creare una matrice NxN e posizionare
gli M fiori in posizioni casuali (distinte tra loro).
I fiori possono essere rappresentati da un valore Booleano True/False.

In seguito, il programma calcoli una matrice NxN di numeri interi,
in cui ciascuna cella contenga il numero di fiori presenti
nelle 8 celle adiacenti (se esistono).
Si stampi il contenuto di queste due matrici,
per verificare la correttezza dei calcoli.

Si permetta poi all'utente di selezionare una casella
(inserendone le coordinate di riga e colonna).
In funzione del contenuto di tale casella, sono possibili i 
seguenti tre casi:
- casella già selezionata in precedenza: si stampi un messaggio di errore
- casella contenente una zolla d'erba: si stampi un messaggio di sconfitta,
    e il numero di fiori nelle caselle adiacenti
- casella contenente un fiore: si stampi il numero di fiori trovati fino a quel momento

Esempio:
🟢🟢🟢🟢  1110
🟢🌸🟢🟢  2121
🌸🟢🟢🌸  1331
🟢🟢🌸🟢  1212

[[False, False, False, False],
[False, True, False, False],
...]

"prato", "prato","prato","prato"
"prato","fiore","prato","prato".
"""

from random import randint

N = 8
M = 4

# Inizializzo la mappa di prato di dimensione NxN tutta False
prato =[]
for i in range(N):
 prato.append([False]*N)

# Abbiamo inserito esattamente m fiori
for j in range(M):
    # Indice casuale
    r = randint(0, N-1)
    c = randint(0, N-1)

    while prato[r][c]:
        # fino a che non becco un False genero posizioni casuali (evito una coppia di r c già uscita)
        r = randint(0, N-1)
        c = randint(0, N-1)

    prato[r][c] = True

for i in range(N):
    for j in range(N):
        if prato[i][j]:
            print("🌸", end="")
        else:
            print("🟢", end="")
    print()

vicini=[]
for i in range(N):
    vicini.append([0]*N)

for r in range(N):
    for c in range(N):
        conta=0
        for i in range(r-1,r+2):
            for j in range(c-1, c+2):
                if 0<= i< N and 0 <= j < N and not(i==r and j==c):
                    if prato[i][j]:
                        conta = conta + 1
        vicini[r][c]=conta
    
for riga in vicini:
    print(riga)

coordinate= input('coordinata: ')