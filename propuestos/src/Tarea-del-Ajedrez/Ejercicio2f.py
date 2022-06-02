from interpreter import draw
from chessPictures import *

# Para la primera mitad del tablero
parte1A = square.join(square.negative())
parte2A = parte1A.horizontalRepeat(4)
parte1B = parte2A.negative()
parcial = Picture(parte2A.img + parte1B.img)

# Para la mitad faltante
total = parcial.verticalRepeat(2)

# Finalmente
draw(total)
