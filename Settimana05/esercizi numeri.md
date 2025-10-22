# es 98

x = 1E in CA2
y = AF in CA2

x = 0001 1110 in CA2
y = 1010 1111 in CA2

x + y
    ' ' ' ' '
  0 0 0 1 1 1 1 0 +
  1 0 1 0 1 1 1 1
  ===============
  1 1 0 0 1 1 0 1

x + y = 1100 1101 = CD

non c'è overflow perché (+)+(-)=(-) è coerente
(in generale quando sommo numeri di segno opposto non ci sarà mai overflow)

# es 97

121_3 = 1 x 3ˆ2 + 2 x 3ˆ1 + 1 x 3ˆ0
      = 9 +       6       + 1
      = 16_10

convertire 16_10 verso la base 7

16 : 7 = 2 R 2  -> peso 7ˆ0
2 :7 =   0 R 2  -> peso 7ˆ1

16_10 = 22_7

15_10 : 7 = 2 R 1
2 :7      = 0 R 2
15_10 = 21_7

# es 96

a = -14
b = 18

a = 1       ? ? ? ? ? 
    -32     32-14 = 18
            1 0 0 1 0

a = 1 1 0 0 1 0       in CA2


|a| = 14
|a| in binario puro = 0 0 1 1 1 0

14 : 2 = 7 R 0
7: 2   = 3 R 1
3: 2   = 1 R 1
1: 2   = 0 R 1
|a| =  1 1 1 0
su 6 bit scrivo 0 0 1 1 1 0

-|a| -> conversione al CA2
- inverto i bit
1 1 0 0 0 1
- sommo 1

1 1 0 0 0 1 + 
0 0 0 0 0 1
-----------
1 1 0 0 1 0 = a in CA2


b = 18

b = 0 1 0 0 1 0

a-b

  1 1 0 0 1 0 -
  0 1 0 0 1 0 
  ===========
  1 0 0 0 0 0

niente overflow perché (-) - (+) = (-) è coerente

a-b = -32



(-14) - (+19)

  ' ' ' ' '
  1 1 0 0 1 0 -
  0 1 0 0 1 1 
  ===========
  0 1 1 1 1 1

Overflow perché il segno + è incoerente
(vale +31 invece del valore "giusto" -33)

# es 95

a = 1AF3
b = 8F02

qual è il maggiore, in CA2 su 16 bit?

a = 0001 1010 1111 0011
b = 1000 1111 0000 0010

a>0 e b<0 ==> a>b


variante:

a = CAF3
b = 8F02

a = 1100 1010 1111 0011  <0
b = 1000 1111 0000 0010  <0

a = 1 100101011110011  <0
b = 1 000111100000010  <0

conclusione : a>b perché la parte positiva
di a è maggiore di quella di b

attenzione: |a|<|b|

# es 94

x = 112_10
y = 76_10

y+x in CA2 su 8 bit

x = 0 1 1 1 0 0 0 0 
112 = 64 + 48 / 48 = 32 + 16
112 = 64 + 32 + 16 = 2ˆ6 + 2ˆ5 + 2ˆ4

y = 0 1 0 0 1 1 0 0
76 = 64 + 12 // 12 = 8 + 4
2ˆ6 + 2ˆ3 + 2ˆ2

  '
  0 1 1 1 0 0 0 0  +
  0 1 0 0 1 1 0 0  =
  ---------------
  1 0 1 1 1 1 0 0

overflow!!
il segno - del risultato non è coerente
con i segni + dei due addendi

112+76 > 127

# es. 93

F     1    A    2
1111 0001 1010 0010

11 11 00 01 10 10 00 10
3  3  0   1  2  2  0  2

1 111 000 110 100 010
1  7   0   6   4   2

# es 90

x = F3

x = 1111 0011

in binario puro:
128+64+32+16+2+1 = 243

in modulo e segno:

1    1110011
(-)  115 (64+32+16+2+1)
cioè -115

in Complemento a 2:
-128 +64+32+16+2+1 = -13