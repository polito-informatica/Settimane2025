infile = open("dati.txt", "r")

lines = infile.readlines()
infile.close()

somma_crediti = 0
somma_voti = 0

for line in lines:
    
    campi = line.split()
    print(campi)
    crediti = campi[1]
    voto = campi[2]

    somma_crediti += int(crediti)
    somma_voti += int(voto)*int(crediti)

media_pesata = somma_voti / somma_crediti
print(media_pesata)


outfile = open("outfile.txt", "w")

for line in lines: 
    #campi = line.split()
    #voto = campi[2]
    voto =line.split()[2]
    print(repr(voto))
    outfile.write(f"{voto}\n")

outfile.close()