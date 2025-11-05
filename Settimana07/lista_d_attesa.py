"""
Gestire la lista d'attesa per un locale.
Le persone in lista sono identificate con il proprio nome, e non ci sono omonimi. 
Il programma prende in input un'operazione che inserisce l'utente, 
la quale in questo caso è la persona che gestisce gli ingressi all'evento. 
Le operazioni da gestire sono le seguenti (i nomi delle persone sono a titolo esemplificativo):

P mina -> restituisci la Posizione di mina (se non è presente, segnalalo)
A pippo -> Aggiungi in coda pippo (se è già presente, segnalalo)
R gina -> Rimuovi dalla coda gina (se non è presente, segnalalo)
I john -> Inserisci in testa john (se è già presente, segnalalo)

Dopo ogni iterazione, il programma restituisce in output la lista d'attesa nel suo stato corrente, con il formato:

1 john
2 gale
3 iram
4 melany
5 pippo

Il programma termina quano viene inserita in input la stringa vuota ("").

"""

persone = ["marco", "anna", "andrea", "elisa","elisa"]

operazione = input("Inserisci operazione: ")

while operazione != "":

    # variabile booleana per validare l'input
    input_valido = True

    parti = operazione.split()

    if len(parti)!=2:
        print("Input non valido: operazione mal strutturata")
        input_valido = False

    if input_valido:
        azione = parti[0].upper()
        persona = parti[1].lower()

        if azione not in ["P", "A", "I", "R"]: #"PAIR": 
            print("Input non valido: azione inesistente")
            input_valido = False

    if input_valido:

        if azione == "P":
            if persona in persone:
                print(f"La posizione di {persona} è {persone.index(parti[1])+1}")
                """
                # VERSIONE CHE GESTISCE GLI OMONIMI
                posizioni = []
                for i, p in enumerate(persone):
                    if p == persona:
                        posizioni.append(i)
                
                print(f"La posizione di {persona} è {posizioni}")
                """
            else:
                print(f"Non posso stampare la posizione perché {persona} non è in lista.")

        elif azione == "A":
            """
            # VERSIONE CHE AMMETTE GLI OMONIMI
            persone.append(parti[1])
            """
            if persona not in persone:
                persone.append(parti[1])
            else: 
                print(f"Non posso aggiungere {persona} perché è già in lista.")

        elif azione == "R":
            if persona in persone:
                persone.remove(persona)
            else:
                print(f"Non posso rimuovere {persona} perché non è in lista.")
        
        elif azione == "I":
            """
            # VERSIONE CHE AMMETTE GLI OMONIMI
            persone.insert(0, persona)
            """     
            if persona not in persone:
                persone.insert(0, persona)
            else:
                print(f"Non posso inserire {persona} perché è già in lista.")
            
        # stampa del contenuto corrente della lista
        print()
        for i, p in enumerate(persone):
            print(i+1, p)
    
    operazione = input("Inserisci operazione: ")
 