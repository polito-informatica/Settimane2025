# citta = ["Torino", "Milano", "Roma", "Napoli", "Palermo"]
# temperature = [15, 18, 22, 24, 26]


temperature_citta = {
    "Torino": 15,
    "Milano": 18,
    "Roma": 22,
    "Napoli": 24,
    "Palermo": 26
}

for citta in temperature_citta:
    print(citta, temperature_citta[citta])

if "Roma" in temperature_citta:
    temp = temperature_citta["Roma"]

print(sorted(temperature_citta))

citta_temperature = {
    15:  "Torino",
    18: "Milano",
    22: "Roma",
    24: "Napoli",
    26: "Palermo"
}

for temp in sorted(citta_temperature):
    print(temp, citta_temperature[temp])


temperature = [
    { 'citta': "Torino", 'temperatura': 15},
    { 'citta': "Milano", 'temperatura': 18},
    { 'citta': "Roma", 'temperatura': 22}
]

temp = -999
for citta in temperature:
    if citta["citta"]=="Roma":
        temp = citta['temperatura']