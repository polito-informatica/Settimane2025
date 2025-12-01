# Es. 1 T1
in CA2 su 8 bit
x = C0
y = 66
x - y

x = 11000000
y = 01100110

x-y 01011010

x-y = 5A
c'è stato overflow perché (-) - (+) non può essere (+)

# Es. 1 T2

x = 366 = 3 * 64 + 6 * 8 + 6
y = 142

numeri in base 8 su 8 bit
possono andare da 000 a 377

x = *11 110 110
y = 01100010

    10 010 100

x-y = 224 senza overflow: (-)-(+)=(-)

# Es. 1 T3

    x = C0
    y = 86

11000000 +
10000110

01000110

overflow perché (-)+(-)= (+)

# Es. 1 T4

    x = 366
    y = 242

11 110 110 +
10 100 010

10 011 000

no overflow perché (-)+(-) = (-)

# Es. 2 T1

DBUS = 64 bit (allineato ai registri)

MEM = 32 GB 
2^ABUS x DBUS = 32 GB

2^ABUS x 2ˆ3 B = 2ˆ5 2ˆ30 B
2^ABUS = 2^(5+30-3) = 2^32
ABUS = 32 bit

# Es. 2 T2

Devo azzerare (32GB/8B = 4G) celle di memoria,
quindi eseguire 4G istruzioni macchina

1 istruzione macchina dura 2 Tck, con Tck = 0.5 ns ==> istr macchina = 1 ns

Tempo totale = 4G x 1 ns ~= 4 s

# Es. 2 T3

ABUS = 28 bit

MEM = 2^ABUS x DBUS = 2^28 x 4 B =
2 ^30 B = 1 GB

# Es. 2 T4

DBUS = 32 bit

2^ABUS x 4 B = 8 G B
2^ABUS = 2^31
ABUS = 31 bit

# Es.3 T1

x assume i valori degli elementi della lista

x assume valori di tuple il cui primo elemento è l'indice (da 0 in poi) ed il secondo elemento è il valore dell'elemento (come nel caso precedente)

# Es.3 T2

nel primo caso l'ultimo elemento viene sostituito da una stringa vuota e la lunghezza della lista rimane invariata

nel secondo la lista si riduce di un elemento, perdendo l'ultimo

# Es.3 T3

a = [2, 4, 5]
b = [7, 8, 9]

nel primo caso aggiungo al fondo di a gli elementi di b (come a.extend(b))
[2, 4, 5, 7, 8, 9]

nel secondo caso creo una lista di 2 elementi che sono a loro volta le liste degli elementi di a e di b
[ [2, 4, 5], [7, 8, 9]]

# Es.3 T4


nomi = ['Ugo', 'Pio', 'Ale' ]

nel primo caso, si sostituisce il primo nome
['A', 'Pio', 'Ale' ]

nel secondo caso, c'è errore perché starei cercando di modificare il primo carattere del primo nome (la 'U' di Ugo)