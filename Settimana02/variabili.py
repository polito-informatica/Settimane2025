# non si possono dichiarare variabili senza inizializzarle
# area 

# posso inizializzare le variabili a valori di default
area = 0
indirizzo = None

# assegno due valori numerici (int), ciascuno ad una variabile
base = 6
altezza = 4

# assegno alla variabile area il valore corrispondente al risultato della moltiplicazione
# tra i valori assegnati a base ed altezza
area = base * altezza

# posso usare valori string
indirizzo = "Corso Castelfidardo"

# posso riassegnare il valore a una variabile senza vincoli di tipo:
# prima era un int, ora è una string
base = "sei"

# fattore_x non è mai stato definito e inizializzato: errore
#risultato = base * altezza + fattore_x 

# se so già che nella mia soluzione il volume di una bottiglia 
# è un'informazione che non varia mai, allora è consuetudine 
# utilizzare una variabile costante per memorizzarla
# Si tratta di una variabile come le altre, non ho errori se 
# la riassegno. Ma il suo uso corretto è inizializzarla una volta 
# e poi non modificarla più. Si riconosce perché, per convenzione,
#  è scritta in MAIUSCOLO. 
VOLUME_BOTTIGLIA = 10 # mL
numero_bottiglie = 3
volume_totale = numero_bottiglie * VOLUME_BOTTIGLIA
print(volume_totale)

# riassegnazione
numero_bottiglie = 10
tipo_bevanda = "soda"

print(numero_bottiglie)
print(tipo_bevanda)

informazione_completa_numerica = numero_bottiglie + 10
print(informazione_completa_numerica)

informazione_completa_testuale = tipo_bevanda + " senza zucchero"
print(informazione_completa_testuale)

# errore: non posso usare l'operatore + con int e string
#informazione_completa_ibrida = n_bottiglie + " senza zucchero"
#print(informazione_completa_ibrida)

# errore: non si inizia mai il nome di variabile con un numero
#1_variabile = 3 
# variabili con nomi composti: snake_case
una_variabile = 3 
# variabili con nomi composti: camelCase
unaVariabile = 3 

# priorità tra operazioni: 
# PEMDAS: Parenthesis, Exponent, Multiply/Divide, Add/Subtract

risultato = 2 * (3 + 7)
print(risultato)

# sarà diverso da..
risultato = 2 * 3 + 7
print(risultato)

# posso assegnare alle variabili valori, risultati di espressioni e...
# valori restituiti da chiamate di funzioni
# ad esempio le funzioni aritmetiche delle librerie Python

n = -5
# abs() calcola il valore assoluto di n
abs_n = abs(n)
print(abs_n)

#errore: devo passare i parametri corretti alle funzioni.
# abs() si aspetta un valore numerico. 
#abs_n = abs("n")


