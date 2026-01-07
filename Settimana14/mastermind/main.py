# Soluzione proposta esercizio "Mastermind"

# Le sequenze da indovinare ed anche i tentativi
# saranno codificati come liste di numeri interi
# [ 1, 3, 7, 5 ]

# ho scartato le altre possibilità
# "1375"
# [ '1', '3', '7', '5' ]

from itertools import permutations

def leggi_sequenze(nome_file):
    # restituisce una lista di liste di 4 interi ciascuna
    sequenze = []
    with open(nome_file, 'r') as f:
        for riga in f:
            codice = list(riga.rstrip('\n')) # ['2', '3', '4', '5']
            for i in range(len(codice)):
                codice[i] = int(codice[i])
            if len(codice)==4:
                sequenze.append(codice)
            else:
                print("Codice di lunghezza errata: ", riga)

    return sequenze



def controlla_tentativo(tentativo, segreto):
    # segreto e tentativo sono due liste di 4 interi
    x = 0
    r_segreto = []  # copia del segreto che NON contiene i numeri giusti al posto giusto
    r_tentativo = []
    for i in range(len(segreto)):
        if segreto[i]==tentativo[i]:
            x = x + 1
        else:
            r_segreto.append(segreto[i])
            r_tentativo.append(tentativo[i])
    
    y = 0

    for i in range(len(r_tentativo)):
        if r_tentativo[i] in r_segreto:
            y = y + 1
            pos = r_segreto.index(r_tentativo[i])
            r_segreto.pop(pos)

    return x, y  # restituisce una tupla con il numero di X ed il numero di Y




    '''
   segreto 2 3 4 5
   tentati 5 4 4 5


   segreto 2 3  
   tentati 5 4  
'''

def stampa_riga(x, y, tentativo):
    print(f'{x}X {y}Y ', end='')
    for val in tentativo:
        print(val, end='')
    print()

def trova_soluzione(segreto):

    print(f'Indovino il numero: {segreto}')

    numeri, c1 = trova_numeri(segreto)

    trovato, c2 = trova_ordine(numeri, segreto)
    print("Trovato", trovato, "in", c1+c2, "tentativi")

def trova_numeri(segreto):

    conta = 0

    pioli = 0
    tentativo = [0,0,0,0]

    for n in range(0, 10):
        # tentativo = [n]*4

        tentativo = tentativo[0:pioli] + [n] * (4-pioli)

        x, y = controlla_tentativo(tentativo, segreto)
        stampa_riga(x, y, tentativo)
        conta = conta + 1

        pioli = x + y

        if pioli ==4:
            break # interrompi il ciclo se hai già trovato i numeri

    return tentativo, conta

def trova_ordine(numeri, segreto):
    conta = 0
    for tentativo in permutations(numeri):
        x, y = controlla_tentativo(tentativo, segreto)
        stampa_riga(x, y, tentativo)
        conta = conta + 1

        if x==4:
            return tentativo, conta

def main():
    sequenze = leggi_sequenze('sequenze.txt')
    print(sequenze)

    for segreto in sequenze:
        trova_soluzione(segreto)


main()


