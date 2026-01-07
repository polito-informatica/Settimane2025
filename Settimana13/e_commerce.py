# Write your solution here, DO NOT START A NEW PROJECT
# ATTENTION: if you create a new project, your exam paper will not be collected
#            and you will be obliged to come in the subsequent exam session
#
# ATTENTION: on Win 10 (Italian keyboard) characters like [ ] { } have to be
#            created using ALTgr+è (e.g. for [ ) and NOT CTRL-ALT-è
#
# ATTENTION: on macOS you have to use CTRL-C and CTRL-V inside the virtual
#            machine and NOT command-C command-V
#
# if your keyboard is broken you can do copy/paste also with mouse
# and you can copy special characters like [ ] { } < > here
#
# Scrivete qui la vostra soluzione, NON CREATE UN NUOVO PROGETTO
# ATTENZIONE: se create un nuovo progetto il vostro compito non sara'
#             raccolto correttamente e dovrete tornare all'appello successivo
#
# ATTENZIONE: su Win 10 (tastiera italiana) i caratteri speciali (es. { ) vanno
#             scritti ad esempio con ALTgr+è (caso di [ ) e NON CTRL-ALT-è
#
# ATTENZIONE: su macOS vanno usati CRTL-C e CTRL-V per il copia incolla
#                       nella macchina virtuale e NON command-C command-V
#
# se la vostra tastiera è guasta potete fare copia/incolla anche con il mouse
# e per i caratteri speciali potete copiare da questi caratteri  [  ]  {  }  <  >
# print(string.punctuation)
## ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~


print(open('ordini.csv', 'r').read())
print()

import csv
from operator import itemgetter

ordini_cliente = {}
spesa_cliente = {}
unita_prodotto = {}
with open('ordini.csv', 'r') as file:

    lettore = csv.DictReader(file)
    print(lettore)
    for ordine in lettore:
        print(ordine)

        prodotto = ordine['Prodotto']
        quantità = int(ordine['Quantità'])
        prezzo= float(ordine['Prezzo unitario'])
        cliente = ordine['Cliente']


        if cliente in ordini_cliente:
            ordini_cliente[cliente] += 1
        else:
            ordini_cliente[cliente] = 1
        


        totale_ordine = quantità * prezzo

        if cliente in spesa_cliente:
            spesa_cliente[cliente] += totale_ordine
        else:
            spesa_cliente[cliente] = totale_ordine
        
        if prodotto in unita_prodotto:
            unita_prodotto[prodotto] += quantità
        else:
            unita_prodotto[prodotto] = quantità



clienti_ordinati = sorted(ordini_cliente.keys())


spesa_ordinata= sorted(spesa_cliente.items(), key = itemgetter(1), reverse = True)

print(unita_prodotto)

prodotti_ordinati = sorted(unita_prodotto.items(), key = itemgetter(1))

print(prodotti_ordinati)