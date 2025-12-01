# Ex 4 T1

print('\n**** TURNO 1 ****')

citta = ["Torino", "Milano", "Roma", "Napoli", "Palermo"]
temperature = [15, 18, 22, 24, 26]

calda = 0
for i in range(len(citta)):
    print(f"{citta[i]} = {temperature[i]} °C")
    if temperature[i] > temperature[calda]:
        calda = i

print(f"La città più calda è {citta[calda]} ({temperature[calda]} °C)")

# Es. 4 T2

print('\n**** TURNO 2 ****')

import math

punti = [[1, 2], [4, 6], [7, 8]]  

for p1 in punti:
    for p2 in punti:
        if p1 != p2:
            dist = math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)
            print(f"Distanza tra {p1} e {p2} = {dist:.2f}")

# Es. 4 T3

print('\n**** TURNO 3 ****')

temperature = [15, 18, 22, 24, 26, 20, 19]

max_media = -300
pos_max = -1

# Alternativa: inizializzo calcolando la media tra le prime 3 temperature
# max_media = sum(temperature[0:3])/3
# pos_max = 1
# poi nel ciclo for posso iniziare il range dalla posizione 2

for pos in range(1, len(temperature)-1):
    media = (temperature[pos]+temperature[pos-1]+temperature[pos+1])/3
    media = sum(temperature[pos-1:pos+2])/3  # alternativa
    if media > max_media:
        max_media = media
        pos_max = pos

print(f"La temperatura massima è nei giorni {pos_max-1}, {pos_max}, {pos_max+1} e vale {max_media:.2f}")

# Es. 4 T4

print('\n**** TURNO 4 ****')

segrete = ["abc12345", "passw0rd", "letmein1", "qwerty12"]
nuova = "abc12346"

# Nota: si dà per scontato che tutte le stringhe abbiano esattamente 8 caratteri

# Verifico innanzitutto se la password compare esattamente nella lista
if nuova in segrete:
    print(f'Passord {nuova} trovata')
else:
    # verifico una ad una, contando i caratteri diversi
    for s in segrete:
        ## conta caratteri diversi tra 'nuova' e 's'
        cnt = 0
        for i in range(len(s)):
            if s[i]!=nuova[i]: # confronta carattere i-esimo
                cnt = cnt + 1
        if cnt==1: # esattamente 1 carattere di differenza
            print(f'Password {nuova} simile a {s}')