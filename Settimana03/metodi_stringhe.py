nome = "Andrea"

# questa operazione non ha particolari effetti se 
# non ne salvo il valore restituito da qualche parte
nome.upper() 

# salvando il valore restituito lo posso poi usare nel mio programma
# tutto maiuscolo 
nome_gridato = nome.upper()
print(nome_gridato)

# la stessa cosa la posso ottenere in modo più compatto
print(nome.upper())

# tutto minuscolo
nome_sussurrato = nome.lower()
print(nome_sussurrato)

# rendere maiuscola l'ultima lettera di una stringa
ultima = nome[len(nome)-1]
ultima_maiuscola = ultima.upper()
print(ultima_maiuscola)
nome = nome[:len(nome)-1] + ultima_maiuscola
print(nome)


#######

# metodi per la ricerca di sottostringhe in una stringa

# restituisce l'indice della prima occorrenza
# dà errore se non ne trova alcuna
nome1 = "Alessandra"
indice = nome1.index("A")
print(indice)

# restituisce l'indice della prima occorrenza
# restituisce -1 se non ne trova alcuna
indice = nome1.find("x")
print(indice)

# un metodo per togliere gli spazi agli estremi di una stringa
parola = " ciao "
parola_stripped = parola.strip()
print(parola_stripped)

# un metodo per sostituire una sottostringa con un'altra
# agisce su tutte le occorrenze all'interno della stringa
parola_alterata = parola.replace("a", "e")
print(parola_alterata)

nome_alterato = nome1.replace("a", "e")
print(nome_alterato)