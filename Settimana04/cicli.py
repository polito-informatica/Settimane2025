# stampa i numeri da 1 a N, con N inserito da tastiera

# print(1)
# print(2)
# print(3)
# ...
# print(10)


# x -> variabile di controllo del ciclo

x = 1   # inizializzazione -> valore che assumerà alla prima iterazione

while x <= 10:  # condizione di iterazione (dipente dalla variabile di controllo 
    # e PRIMA O POI DEVE diventare False)

    print("*")   # corpo del ciclo (posso usare oppure no la variabile di controllo)

    x = x + 1 # aggiornamento della variabile di controllo

print("finito")

# Stampa i quadrati dei primi N numeri interi

N = int(input("valore di N: "))

c = 1
while c  <= N :
    quadrato = c * c
    print( c, quadrato )
    c = c + 1


i = 0
while i < N:

    numero = i+1
    quadrato = numero*numero
    print(quadrato)

    i = i + 1


# stampa i quadrati dei primi N numeri dispari

print("Stampa dei primi numeri dispari")

i = 0
numero = 1

while i < N:

    quadrato = numero*numero
    print(numero, quadrato)
    numero = numero + 2

    i = i + 1   # 'contatore'

# quadrato = 1
# while quadrato <= N*N:
#     print(quadrato)
#     quadrato = ????


