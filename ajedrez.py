from random import randint, sample
from os import supports_effective_ids, terminal_size

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
def print_tablero(tablero):
    for i in range(9):
        print(tablero[i])
        
print_tablero(tablero)
        
    
def movimientos_ficha(tablero):
    while True:
        ficha = input("Elige la ficha que deseas mover seleccionando sus coordenadas por separado:") #se lo pido al usuario
        ficha = ficha.split() # Devuelve la variable ficha usando como delimitador la cadena delimitador. Si no se especifica el delimitador utiliza por defecto el espacio en blanco
        if len(ficha) == 2: #'len' va a contar la cantidad de numeros introducidos y si es == 2, entonces seguira el bucle
            filaI = ficha[0]
            columnaI = ficha[1]
            try:
                filaI = int(filaI)
                columnaI = int(columnaI)
            except:
                pass
            else:
                if filaI >= 0 and filaI < 8 and columnaI >= 0 and columnaI < 8:
                    break
    while True:
        recorrido = input("Elige las coordenadas a las que deseas mover tu ficha:")
        recorrido = recorrido.split()
        if len(recorrido) == 2:
            filaE = recorrido[0]
            columnaE = recorrido[1]
            try:
                filaE = int(filaE)
                columnaE = int(columnaE)
            except:
                pass
            else:
                if filaE >=0 and filaE < 8 and columnaE >=0 and columnaE < 8 and recorrido != ficha:
                    (tablero[filaE])[columnaE] = tablero[filaI][columnaI]
                    (tablero[filaI][columnaI]) = " "
                    break
            