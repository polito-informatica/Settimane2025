# Esercizi Architetture

# 97

registri interni alla CPU contengono dati di ingresso e risultati delle operazioni della ALU/FPU.
Composti di memoria con tempi di risposta pari al tempo di elaborazione delle operazioni.

# 96

è la fase nella quale a partire dal valore del Program Counter , si indirizza la memoria per ottenere il codice binario della prossima istruzione da eseguire, memorizzandono nell'Instruction Register
IR <- MEM(PC)

# 95 

M = 1 kB
DBUS = 8 bit
ABUS = ?


parallelismo della memoria = DBUS = dimensione registri dati

n.celle memoria centrale <= 2 ^ ABUS

MEM = 2 ^ ABUS x DBUS


M = 1 kB
DBUS = 8 bit = 1 byte 
M ha celle da 1 byte
M in totale ha 1k celle = 1024 celle = 2ˆ10
ABUS = 10

# 94

ABUS = 20 bit
parallelismo = 4 byte (B) = 32 bit (b)

Max mem = 2^ABUS x 4 Byte = 2ˆ20 x 4 B = 2ˆ22 B = 4 MB

se avessi 1 in bit in più nell'ABUSm la mem max raddoppierebbe (2ˆ23 B  = 8 MB)

# 93

eseguire tutte le operazioni artimetiche e logiche, partendo dagli operandi prenentei nei registri e salvando il risultato in un registro. Inoltre aggiorna il registro dei FLAG.

0001 + 1000 -> ALU -> 1001 / Z=0 V=0 S=1 C=0

# 91 

UC contiene i registri PC e IR, nonché la logica per gestire il ciclo di esecuzione delle istruzioni 

# 89

UO = Registri + ALU

# 88

MEM MAX = 2 ^ ABUS x DBUS

# 87

registro che memorizza l'inrizizzo di memoria della prossima istruzione da eseguire.
Viene usato nella fase di fetch e poi incrementato di 1.

# 86

Fetch 
Decode
Execute

# 85

perché sono più facili
 nei numeri reali devo operare separatamente su mantissa ed esponente

# 84

f_CK = 2 GHz
T_CK = 0.5 ns = 500 ps

1 operazione ogni 4 CK

n.operazioni = 10 milioni = 10ˆ7

t totale = n.operazioni x durata di 1 operazione

durata 1 operazione = 4 x T_CK = 2 ns

t tot = 10ˆ7 x 2 ns = 0.02 s = 20 ms

# 83

Registri
Cache (1 e 2 livello)
Memoria centrale (RAM)

Memorie di massa

# 82

Memoria RAM / Memoria centrale
contiene i programmi in esecuzione
contiene i dati su cui tali programmi lavorano

La cache contiene delle COPIE dei dati della RAM che vengono letti/scritti dalla CPU. Scopo: accelerare le operazioni di accesso

# 80

ABUS - Address
    trasporta l'indirizzo di memoria di una cella da leggere/scrivere
DBUS - Data
    trasporta un dato letto dalla memoria e diretto alla CPU o fornito dalla CPU e scritto in memoria
CBUS - Control
    indica l'operazione che memoria deve fare (lettura/scrittura) e la tempistica con cui avviene (clock dei bus)

# 79
eseguono op aritmetiche e logiche
ALU su quantità intere
FPU su numeri floating point (anche op. algebriche esponenziali trigonometriche)

# 78

MEM = 1 MB
DBUS = 32 bit

2^ABUS x DBUS = MEM
2^ABUS x 32 b = 1 M x 8 b
2^ABUS = 1 M x 8 b / 32 b
2^ABUS = 2^18
ABUS = 18 bit

# 73

parametri : 
    velocità di risposta
    capacità di memorizzazione
    costo

    parallelismo
    lettura / lettura-scrittura
    volatilità

# 66

svantaggio: impossibile fare più trasferimenti in parallelo => rallenta nel caso di molti trasferimenti necessari

vantaggio: costo minore, espandibilità

# 64

RAM = 128 kB
ABUS = 12 bit
celle = ?

tot celle = 2 ˆ 12 = 4 k

dimensione cella = tot memoria / tot celle
= 128 k B / 4 k = 32 B = 32 byte = 256 bit

# 57

operazioni tra interi
operazioni tra numeri reali
lettura/scrittura di un dato in memoria
lettura/scrittura da I/O

# 55

ABUS = 10 bit

cell memoria = 2 ^ 10 = 1k 

Max memoria = 1k celle x 2B/cella = 2 kB

# 54

Fetch:
    ABUS = PC
    CBUS = lettura da memoria
    DBUS = istruzione (finirà nel IR)
Decode:
    niente
Execute:
    niente per operazioni (es.) aritmetiche

    per operaizoni di trasf. dati
    lettura:
        ABUS = inidirzzo variabile da leggere
        CBUS = leggi
        DBUS = dato proveniente da memoria
    scrittura
        ABUS = indirizzo variabile da modificare
        CBUS = scrivi
        DBUS = valore (preso da un registro) che dovrà essere memorizzato

# 51

MEM = 64 GB RAM
MEM = 4 GB cache (non conta, non è indirizzabile direttamene)

cella = 128 bit

2^ABUS x cella = MEM

2 ^ ABUS x 128 b = 64 G B
2 ^ ABUS x 2^7 b = 2^6 2^30 2^3 b

2 ^ ABUS = 2 ^ 32
ABUS = 32

