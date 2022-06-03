from interpreter import draw
from chessPictures import *

#por separado
filaPGrandes = rock.join(knight.join(bishop.join(queen.join(king.join(bishop.join(knight.join(rock)))))))
filaPPeon = pawn.horizontalRepeat(8)

blancas = Picture(filaPPeon.img + filaPGrandes.img)
negras = Picture(filaPGrandes.img + filaPPeon.img).negative()

# Partes del tablero
parte1A = square.join(square.negative())
parte2A = parte1A.horizontalRepeat(4)
parte1B = parte2A.negative()
#
parcial = Picture(parte2A.img + parte1B.img)
#                                   ............Parte 2
total = parcial.verticalRepeat(2)

# De las negras : negras sobre parcial..........Parte 1
eNegras = negras.up(parcial)
# De las blancas : blancas sobre parcial........Parte 3
eBlancas = blancas.up(parcial)

# Armando el tablero:
tablero = Picture(eNegras.img + total.img + eBlancas.img)

draw(tablero)