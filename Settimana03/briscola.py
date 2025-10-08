## Lettura dei dati (input)

briscola = input("Seme di briscola: ")   # 'C'
carta1 = input("Carta primo giocatore: ")  # '3P'
carta2 = input("Carta secondo giocatore: ") # '4C'

# TODO: verificare la correttezza dei dati di ingresso

valore1 = carta1[0]
valore2 = carta2[0]

seme1 = carta1[1]
seme2 = carta2[1]

# # converto i valori in punteggi ==> si può fare come soluzione alternativa
# 'A' -> 11
# 'J' -> 2
# '3' -> 10
# '2' -> 0
# '4' -> 0

# # converto i valori in numeri d'ordine ==> implementiamo questa opzione
# '2'-> 1
# '4'-> 2
# '5'-> 3
# ...
# 'J'-> 6
# 'Q'-> 7
# 'K'-> 8
# '3'-> 9
# 'A'-> 10

ordine_crescente = '24567JQK3A'
# le posizioni di indici maggiori corrispondo a carte di valore maggiore

ordine1 = ordine_crescente.find(valore1)
ordine2 = ordine_crescente.find(valore2)

# if valore1 == '2':
#     ordine1 = 1
# elif valore1 == '4':
#     ordine1 = 2
#     ....
# e poi:
# if valore2 == '2':
#     ordine2 = 1
# elif valore2 == '4':
#     ordine2 = 2
#     ....



# una carta con il seme di briscola vince sempre su una carta di seme diverso
# caso 1. carta1 è di briscola, carta2 no -> vince 1
if seme1==briscola and seme2!=briscola:
    print(f'Vince: {carta1}')
elif seme2==briscola and seme1!=briscola:
    print(f'Vince: {carta2}')
elif seme1 != seme2:
    print(f'Vince: {carta1}')
else:
    # se arrivo qui, so di sicuro che hanno lo stesso seme
    # (può essere briscola oppure no)
    if ordine1>ordine2:
        print(f'Vince {carta1}')
    else:
        print(f'Vince {carta2}')


# A 2 3 4 5 6 7 J Q K
# ordine lessicografico sono:
# 2 3 4 5 6 7 A J K Q






## Stampa del vincitore