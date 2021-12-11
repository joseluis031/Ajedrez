from random import randint, sample
tablero =[
    [' ','1','2','3','4','5','6','7','8'],
    ['1',' ',' ',' ',' ',' ',' ',' ',' '],
    ['2',' ',' ',' ',' ',' ',' ',' ',' '],
    ['3',' ',' ',' ',' ',' ',' ',' ',' '],
    ['4',' ',' ',' ',' ',' ',' ',' ',' '],
    ['5',' ',' ',' ',' ',' ',' ',' ',' '],
    ['6',' ',' ',' ',' ',' ',' ',' ',' '],
    ['7',' ',' ',' ',' ',' ',' ',' ',' '],
    ['8',' ',' ',' ',' ',' ',' ',' ',' '],
]
#dibujo de las fichas
REY_BLANCO = chr(0x2654)
REINA_BLANCO = chr(0x2655)
TORRE_BLANCO = chr(0x2656)
ALFIL_BLANCO = chr(0x2657)
CABALLO_BLANCO = chr(0x2658)
PEÓN_BLANCO = chr(0x2659)

REY_NEGRO = chr(0x265A)
REINA_NEGRO = chr(0x265B)
TORRE_NEGRO = chr(0x265C)
ALFIL_NEGRO = chr(0x265D)
CABALLO_NEGRO = chr(0x265E)
PEÓN_NEGRO = chr(0x265F)

#posicion inicial fichas blancas
(tablero[8])[5] = REY_BLANCO
(tablero[8])[4] = REINA_BLANCO
(tablero[8])[1] = TORRE_BLANCO
(tablero[8])[8] = TORRE_BLANCO
(tablero[8])[3] = ALFIL_BLANCO
(tablero[8])[6] = ALFIL_BLANCO
(tablero[8])[2] = CABALLO_BLANCO
(tablero[8])[7] = CABALLO_BLANCO
(tablero[7])[1] = PEÓN_BLANCO
(tablero[7])[2] = PEÓN_BLANCO
(tablero[7])[3] = PEÓN_BLANCO
(tablero[7])[4] = PEÓN_BLANCO
(tablero[7])[5] = PEÓN_BLANCO
(tablero[7])[6] = PEÓN_BLANCO
(tablero[7])[7] = PEÓN_BLANCO
(tablero[7])[8] = PEÓN_BLANCO

#posicion inicial fichas negras
(tablero[1])[5] = REY_NEGRO
(tablero[1])[4] = REINA_NEGRO
(tablero[1])[1] = TORRE_NEGRO
(tablero[1])[8] = TORRE_NEGRO
(tablero[1])[3] = ALFIL_NEGRO
(tablero[1])[6] = ALFIL_NEGRO
(tablero[1])[2] = CABALLO_NEGRO
(tablero[1])[7] = CABALLO_NEGRO
(tablero[2])[1] = PEÓN_NEGRO
(tablero[2])[2] = PEÓN_NEGRO
(tablero[2])[3] = PEÓN_NEGRO
(tablero[2])[4] = PEÓN_NEGRO
(tablero[2])[5] = PEÓN_NEGRO
(tablero[2])[6] = PEÓN_NEGRO
(tablero[2])[7] = PEÓN_NEGRO
(tablero[2])[8] = PEÓN_NEGRO
#printeo el tablero
for i in range(9):
    print(tablero[i])