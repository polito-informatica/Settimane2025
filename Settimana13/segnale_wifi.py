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


print(open('segnale.txt', 'r').read())
print()
print(open('zone.txt', 'r').read())
print()


with open('segnale.txt', 'r') as f:
    segnale_lines = f.readlines()

with open('zone.txt', 'r') as f:
    zone_lines = f.readlines()


segnale = []
zone = []

for line in segnale_lines:
    riga = line.strip().split()
    segnale.append(riga)

for line in zone_lines:
    riga = line.strip().split()
    zone.append(riga)

print(segnale)
print(zone)

zona_dati = {}

for i in range(len(zone)):
    for j in range(len(zone[i])):
        zona_carattere = zone[i][j]
        segnale_valore = segnale[i][j]

        if zona_carattere != '-':
            valore = float(segnale_valore)

            if zona_carattere not in zona_dati:
                zona_dati[zona_carattere] = []
            
            zona_dati[zona_carattere].append(valore)

print(zona_dati)


zona_statistiche = {}
min_globale = float('inf')
max_globale = float('-inf')

for zona ,valori in zona_dati.items():
    minimo = min(valori)
    massimo = max(valori)
    media = sum(valori)/len(valori)

    zona_statistiche[zona] = {
            'min': minimo,
            'max': massimo,
            'media': media
    }
    
    if minimo < min_globale:
        min_globale= minimo
    if massimo > max_globale:
        max_globale=massimo

print(min_globale,max_globale)

escursione = max_globale - min_globale

zone_ordinate = sorted(zona_statistiche.keys())

print(f"Zona\tS.Min\tS.Max\tS.Medio")
for zone in zone_ordinate:
    stats = zona_statistiche[zone]
    print(f"{zone}\t{stats['min']:.1f}\t{stats['max']:.1f}\t{stats['media']:.1f}")

print(f"Escirssione: {escursione}")