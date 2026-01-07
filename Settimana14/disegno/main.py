# Soluzione proposta esercizio "Disegno"

"""
la struttura dati sarà una matrice 10x10 in cui ciascuna cella conteine
una stringa di 1 carattere da "0"a "9".

Le immagini lette da file possono contenere anche "X", ma quella finale no.

finale = [ 
    ['9', '9', '9', '9'],
    ['9', '9', '9', '9', ]
    [9,9,9,9]
]

Le operazioni le rappresento come dizionari { 'file': 'img1.txt', 'riga': 2, 'col': 0 }
"""

DIM = 10

def main():
    finale = inizializza_immagine()
    # visualizza(finale)

    operazioni = leggi_operazioni('input.txt')
    # print(operazioni)

    file_max_dim = ''
    max_dim = 0

    min_scuro = 10.0
    file_min_scuro = ''

    for op in operazioni:
        immagine = leggi_immagine(op['file'])

        dim = len(immagine) * len(immagine[0])
        if dim>max_dim:
            max_dim = dim
            file_max_dim = op['file']

        media_scuro = scuro(immagine)
        if media_scuro<min_scuro:
            min_scuro = media_scuro
            file_min_scuro = op['file']


        # print(immagine)
        # visualizza(immagine)

        sovrapponi(finale, immagine, op['riga'], op['col'])  # modifica l'immagine 'finale' incollando i pixed dell'immagine
    
    print('Numero di immagini di input: ', len(operazioni))
    print('Immagine più grande: ', file_max_dim)
    print('Immagine più scura: ', file_min_scuro, f'{min_scuro:.2f}')

    visualizza(finale)

def inizializza_immagine():
    img = []
    for i in range(DIM):
        riga = [ '9' ] * DIM
        img.append(riga)
    return img

def leggi_operazioni(nome_file):
    operazioni = []
    with open(nome_file, 'r') as f:
        for riga in f:
            campi = riga.rstrip('\n').split()
            operazioni.append({
                'file': campi[0],
                'riga': int(campi[1]),
                'col': int(campi[2])
            })
    return operazioni

def leggi_immagine(nome_file):
    img = []
    with open(nome_file, 'r') as f:
        for riga in f:
            pixel = list(riga.rstrip('\n'))
            img.append(pixel)
    return img

def sovrapponi(finale, immagine, riga, col):
    # r, c: riga e colonna dentro 'immagine'
    for r in range(len(immagine)):
        for c in range(len(immagine[r])):
            pixel = immagine[r][c]
            if pixel != 'X':
                finale[riga+r][col+c] = pixel

def visualizza(immagine):
    for riga in immagine:
        for col in riga:
            print(col, end='')
        print()

def scuro(immagine):
    somma = 0.0
    num = 0

    for r in immagine:
        for pix in r:
            if pix!='X':
                somma = somma + int(pix)
                num = num + 1

    return somma / num

main()