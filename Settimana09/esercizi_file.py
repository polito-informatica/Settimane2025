infile = open("Settimana09/testo.txt", "r")
outfile = open("outfile.txt", "w")

lines = infile.readlines()
outfile.writelines(lines)

infile.close()
outfile.close()



