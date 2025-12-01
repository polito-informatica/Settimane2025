# Simulazione della prova in itinere

persone = [ 'Gigi', 'Franco', 'Pier Carlo', 'Piercarlo', 'Antonio', 'Franco', 'Ugo', 'Carlo Maria', 'Stefano ']

altra = []
for p in persone:
    if len(p)>4 and (' ' not in p):
        if p not in altra:
            altra.append(p)

print(altra)