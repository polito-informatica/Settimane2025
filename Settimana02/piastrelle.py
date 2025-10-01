import math


MURO = 100
PIASTRELLA = 5

# numero di pastrelle se non ci fossero vincoli, 
# con anche una parte frazionaria
x = MURO / PIASTRELLA

# bla bla bla -> ragionamento che spiega cosè la formula
n_piastr_totali =  int(x) - (1 - (int(x) % 2))
# DI SICURO è un numero dispari

# n_nere = math.ceil(n_piastr_totali/2)
# n_bianche = math.floor(n_piastr_totali/2)

n_bianche = (n_piastr_totali-1) // 2
n_nere = (n_piastr_totali+1) // 2
# n_nere = n_bianche + 1
# n_nere = n_piastr_totali - n_bianche

print("Nere:", n_nere)
print("Bianche:", n_bianche)

vuoto = (MURO - n_piastr_totali * PIASTRELLA)/2

print("Spazio vuoto:", vuoto)

