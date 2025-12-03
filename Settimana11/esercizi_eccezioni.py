# Alcuni tipi di eccezioni: 
#
# - ValueError: ad es, errori di conversione
# - IndexError: ad es, indici di liste fuori dal range
# - FileNotFoundError: ad es, si prova ad aprire un file in lettura che non è presente

# Situazioni in cui è tipico dover gestire eccezioni

# Lettura file
# Lettura input

try:
    with open("dati_sensori.csv", "r") as f:
        print(f.readline())
    n = int(input("Inserisci un numero: "))
except FileNotFoundError as fnfe:
    print("Qualche problemino con l'apertura del file: ", fnfe)
except ValueError as ve:
    print("Il problema qui è legato ai valori...")

print("Sono arrivata fino qui!")






try: 
    out_f = open("output_file.csv", "w")
    in_f = open("dati_sensori2.csv", "r")
    
except FileNotFoundError as e:
    print("Non c'è il file!")
finally:
    print("Ora chiudo il file")
    out_f.close()


