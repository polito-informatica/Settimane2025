"""
Partendo dall'esercizio "briscola" della Settimana 03, estendiamolo 
in modo da poter gestire un mazzo completo di carte e gestire lo 
svolgimento di una partita.

In particolare, si realizzino le seguenti operazioni:

- creare un mazzo di carte che contiene tutte le possibili carte di gioco

- mescolare il mazzo in ordine casuale

- identificare il seme di briscola dalla prima carta del mazzo 
(che poi va inserita per ultima)

(opzionale)
- simulare una serie di mani di gioco, in cui si supponga di avere 2 giocatori, che peschino e
giochino una carta ciascuno. Si ricordi che il primo giocatore a pescare e giocare è sempre
quello che ha vinto la mano precedente.
"""

'''

singola carta = "3F"
mazzo di carte = [ "3F", "AP", "QQ" ] -> una lista di stringhe, ciascuna rappresenta una carta


'''

import random


VALORI = '24567JQK3A'   # valori delle carte, in ordine di vittoria
SEMI = 'CQFP'

# SEMI = [ 'C', 'Q', 'F', 'P' ]

# creiamo un mazzo nuovo

mazzo = []

for valore in VALORI:
    for seme in SEMI:
        # print(valore, seme)
        mazzo.append( valore+seme )

# print(mazzo)

# mescola il mazzo

mazzo_rimescolato = []
temp_mazzo = list(mazzo)
# temp_mazzo = mazzo NOOO

# while len(temp_mazzo)>0:

while temp_mazzo:
    # pesco una carta a caso dal mazzo
    pos = random.randint(0, len(temp_mazzo)-1)
    carta = temp_mazzo[pos]

    # carta = random.choice(temp_mazzo) 
    # possibile, ma mi mancherebbe il 'pos' e quindi dovrei usare remove anziché pop

    mazzo_rimescolato.append(carta)

    # mazzo.remove(carta)
    temp_mazzo.pop(pos)

print(mazzo_rimescolato)

# alternativa
# mazzo_rimescolato = list(mazzo)
# random.shuffle(mazzo_rimescolato)



'''

mazzo_rimescolato = []

while len(mazzo_rimescolato)<len(mazzo):

# for i in range(len(mazzo)): # perché so già quante iterazioni farò
    # pesco una carta a caso dal mazzo
    pos = random.randint(0, len(mazzo)-1)
    carta = mazzo[pos]

    # if la carta ce l'ho già 
    while carta in mazzo_rimescolato:
        # ne pesco una nuova
        pos = random.randint(0, len(mazzo)-1)
        carta = mazzo[pos]

    mazzo_rimescolato.append(carta)

'''

'''
mazzo_rimescolato = []
c = 0
while len(mazzo_rimescolato)<len(mazzo):
    c = c+1
    # pesco una carta a caso dal mazzo
    pos = random.randint(0, len(mazzo)-1)
    carta = mazzo[pos]

    if carta not in mazzo_rimescolato:
        mazzo_rimescolato.append(carta)

print("Iterazioni", c)

print(mazzo_rimescolato)
print(sorted(mazzo_rimescolato))
'''


# Definisci il seme di briscola

# carta = mazzo_rimescolato[0]
# mazzo_rimescolato.pop(0)

carta = mazzo_rimescolato.pop(0)

seme_briscola = carta[1]


mazzo_rimescolato.append(carta)
mazzo_rimescolato.insert(carta, len(mazzo_rimescolato))