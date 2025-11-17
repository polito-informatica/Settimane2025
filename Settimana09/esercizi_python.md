# Esercizi sulla parte di teoria relativa al linguaggio Python

> Esercizi tratti da: https://github.com/polito-informatica/Esempi-esame/blob/master/teoria/python.md

# 89

enumerate(lista) restituisce una sequenza di coppie (indice, valore), dove l'indice varia da 0 a len(lista)-1 e valore è l'elemento corrispondente a lista[indice].
Utile in un ciclo for su cui vogliamo iterare su una lista, per avere ad ogni iterazione sia l'indice sia il valore dell'elemento.

es..

for i, x in numeri:
    print('alla posizione', i,  "c'è il valore", x)


# 79

Si intende il rientro di un gruppo di righe di codice (inserendo spazi iniziale) e serve a delimitare l'inizio e la fine dei BLOCCHI che costituiscono il corpo delle istruzioni di controllo if: elif: while: for: eccetera.

# 77

x = float(input('x'))
y = float(input('y'))
print(x/y)

Possibili eccezioni:
- float riceve una stringa che NON è formattata come un numero (ValueError)
- x/y se y==0 genera errore (ZeroDivisionError)

# 71

enumerate() -> v. sopra

# 67

Tuple e liste sono entrambi contenitori ordinati accessibili con indice 0...len-1.
Le liste sono mutabili (posso aggiungere cancellare modificare elemnti), mentre le tupe sono immutabili (posso solo assegnare il valore iniziale e non più modificare né il numero né il valore degli elementi).

# 65 

a[0] = 'm''

non è possibile farlo con b perhé le stringhe sono immutabili

b = 'm' + b[1:] non è la stessa cosa perché costruisce una NUOVA stringa

# 61

La stringa non si può convertire nel senso di modificarla (è immutabile!).
Si può costruire una nuova stringhe che sia in maiuscolo con
    s = s.upper()

# 60 

La funzione input() restituisce SEMPRE una stringa.

a = input() # intero
b = input() # decimale
c = int(a) + float(b)

# 55

Dati immutabili: stringhe, tuple

s = "sono immutabile"

s = "anche io"

t = (14, 22)
t[0] =7  #  NO
t = 7 # ok

# 47

L'errore è l'istruzione
        a = a.append(i)
perché append modifica la lista ma non ritorna nessun valore, quindi dalla seconda iterazione 'a' non sarà più la lista ma sarà None, e ovviamente non si potrà più fare append su un oggetto None.

    a.append(i)

    a = a + [i]

# 46

s = input()

Sbagliato:
if s.isnnumeric():
if s.isdigit():

"234" True
"2R22" False

Risposta possibile:
if s.isdigit() or
   (s[0]=='-' and s[1:].isdigit()):

ALtra risposta:

try:
    x = int(s)  # verifica se genera una eccezione
except:
    print('non è intero')

# 41

c='3'
v = int(c)

# 34

gli operatori booleani sono
    and, or, not

if voto>=18 and voto <=30:
    print("ok")

# 32

data lista
a = [ 1, 2, 3]

alias è:
b = a
le variabili a e b fanno riferimento alla stessa lista, la modifica dei valori attraverso a ed attraverso b risulta visibile anche attraverso l'altra variabile. Non abbiao creato una lista nuova ma un nuovo nome ad una lista esistente.

copia è:

c = list(a)
c = a[:]

in questo caso si crea un nuova lista che viene inizializzata con gli stessi elementi (alias) di a, ma che poi avrà vita indipendente

c[0] = a[0]
c[1] = a[1]
c[2] = a[2]

# 30

if a>0:
    print('positivo')
elif a==0:
    print('nullo)
else:
    print('negativo')

# 27 

Sbagliato:

if a==b:

Giusto:

import math
if math.isclose(a,b):

if abs(a-b)<0.001:

