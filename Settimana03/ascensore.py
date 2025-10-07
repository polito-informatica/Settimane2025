piano = int(input("A che piano vuoi andare? "))

if piano<13:
    # caso "normale", quando piano < 13
    piano_reale = piano

if piano>13:
    # caso "speciale" quando piano > 13
    piano_reale = piano - 1 

print("Bisogna spostare l'ascensore al piano ", piano_reale)


if piano<13:
    piano_reale = piano
else:
    piano_reale = piano - 1



## Gestisco il caso in cui, se inserisce 13, stampo errore

if piano < 13:
    piano_reale = piano
else:
    if piano == 13:
        print("Piano non valido")
    else:
        piano_reale = piano - 1

if piano==13:
    print("Piano non valido")
else:
    if piano<13:
        piano_reale = piano
    else:
        piano_reale = piano - 1

if piano == 13:
    print('Non valido')
elif piano < 13:
    piano_reale = piano
else:
    piano_reale = piano - 1
