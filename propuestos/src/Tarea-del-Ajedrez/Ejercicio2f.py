from interpreter import draw
from chessPictures import *

# Para la primera mitad del tablero
parte1A = square.join(square.negative())
parte2A = parte1A.horizontalRepeat(4)

# Para la mitad faltante
parteB = parte2A.verticalRepeat(2)

dibFinal = Picture(parte2A.img + parteB.img)
