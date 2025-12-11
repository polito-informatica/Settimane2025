## Leggi il contenuto del file che rappresenta l'elenco degli studenti
## in una LISTA DI DIZIONARI (ciascun dizionario della lista rappresenta
## un singolo 'record', ossia una riga del file)

import operator


def leggi_studenti(nome_file):
    studenti = []

    with open(nome_file, 'r', encoding='utf-8') as f:
        f.readline() # leggo e ignoro la prima riga

        for riga in f:
            campi = riga.rstrip('\n').split(',')

            studente = {
                'matricola': int(campi[0]),
                'cognome': campi[1],
                'nome': campi[2],
                'email': campi[3]

                # 'nome': campi[1]+ ' ' + campi[2] ,
            }

            studenti.append(studente)

    return studenti

studenti = leggi_studenti('studenti.csv')
# print(studenti)

# trova lo studente con il cognome più lungo

pos_max = 0

for i in range(1, len(studenti)):
# for i in range(len(studenti)-1, 0, -1): ## se volessi trovare l'ultimo
    # if len(cognome dello studente i-esimo) >
    # len(studente in posizione pos_max):
    if ( len(studenti[i]['cognome']) >
        len(studenti[pos_max]['cognome'])) :
        pos_max = i

print(studenti[pos_max])

# metto in ordine di matricola (ci provo...)
studenti.sort(key=operator.itemgetter('cognome'))

print(studenti)

'''
matricole = []
for studente in studenti:
    matricole.append(studente['matricola'])
matricole.sort()
print(matricole)
'''