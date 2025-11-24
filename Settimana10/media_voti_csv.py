import csv

NOMEFILE = 'voti.csv'

f = open(NOMEFILE, 'r', encoding='utf-8')
reader = csv.reader(f)

# costruisco una tabella, in cui le righe sono i singoli esami
# e le 3 colonne sono i campi (nome, crediti, voto)

voti = []

for campi in reader :
    campi[1] = int(campi[1])
    campi[2] = int(campi[2])
    voti.append(campi)

f.close()

somma_voti = 0
somma_cfu = 0
for voto in voti:
    somma_voti = somma_voti + voto[2]*voto[1]
    somma_cfu = somma_cfu + voto[1]

print("Media = ", somma_voti/somma_cfu)