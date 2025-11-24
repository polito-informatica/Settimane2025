# Calcola densità di popolaizone degli stati


FILE_POPOLAZIONE = 'worldpop.txt'
FILE_SUPERFICIE = 'worldarea.txt'


nazioni = []

'''
Voglio costruire una tabella di questo tipo

nazioni = [
 [ NAZIONE,  POPOLAZIONE, SUPERFICIE ] ,
 [ NAZIONE,  POPOLAZIONE, SUPERFICIE ] 
]
'''


'''
Come primo passo, inizio a costruire una tabella con 2 colonne: NAZIONE, POPOLAZIONE
leggendo il primo file
'''
with open(FILE_POPOLAZIONE, 'r', encoding='utf-8') as f:
    for riga in f:
        campi = riga.rstrip().split()   # campi separati da spazio (uno o più spazi o tab)
        popolazione = int(campi[-1])    # l'ultimo campo è sempre la popolazione
        nazione = " ".join(campi[:-1])  # tutti i campi tranne l'ultimo vanno ri-concatenati insieme, unendoli con uno spazio
        nazioni.append( [nazione, popolazione] )

'''
Il secondo passo deve leggere il secondo file, estrarre la SUPERFICIE
ed aggiungere ad ogni riga della tabella il dato corrispondente.
Attenzione: mentre leggo le righe del file, dovrò avanzare la riga della tabella.
'''

