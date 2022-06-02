from interpreter import draw
from chessPictures import *

# Para la primera mitad del tablero
parte1A = square.join(square.negative())
parte2A = parte1A.horizontalRepeat(4)
parte1B = parte2A.negative()

# Para la mitad faltante
total = parte1B.verticalRepeat(2)

# Finalmente
draw(total)
