infile = open("poesia.txt", "r")
outfile = open("parole.txt", "a")

righe = infile.readlines()
infile.close()


for riga in righe: 
    parole_riga = riga.split()
    for parola in parole_riga:
        outfile.write(f"{parola}\n")

outfile.close()