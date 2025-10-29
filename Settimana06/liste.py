a = [ 33, 42, -8, 0, 55 ]

print(a)

# for i in range(len(a)):
#     print(a[i])

# for x in a:
#     print(x)

# Incrementa i valori presenti in a di 3 unità

v = 6
v = v+6

print("Incremento di 3")

print("Prima", a)

for i in range(len(a)):
    x = a[i]
    x = x+3
    a[i] = x
    # a[i] = a[i]+3

print("Dopo", a)

print("Prima", a)

for x in a:
    x = x+3

print("Dopo", a)

# somma dei valori di una lista
somma = 0
for x in a:
    somma = somma + x

print("a coppie")
for i, x in enumerate(a):
    print(i, x)