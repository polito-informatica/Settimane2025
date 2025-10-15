# Leggere un valore intero dall'utente, nel caso in cui non sia un
# numero intero, chiedere di re-inserire il valore

# risposta = input("Inserisci un numero: ")
# if risposta.isnumeric():
#     numero = int(risposta)
#     print(numero)
# else:
#     ripeti l'input

risposta = input("Inserisci un numero: ")
while not risposta.isnumeric():  # condizione di validazione del dato
    print(f'Valore {risposta} non valido, riprova')
    risposta = input("Inserisci un numero: ")

numero = int(risposta)
print(numero)