from interpreter import draw
from chessPictures import *

# Para la primera mitad del tablero
parte1A = square.join(square.negative())
parte2A = parte1A.horizontalRepeat(4)
parte1B = square.negative().join(square)
parte2B = parte1B.horizontalRepeat(4)
primera = (parte1A.img + parte1B.img)

# Para la mitad faltante
segunda = primera.verticalRepeat(2)

# Finalmente
draw(Picture(segunda.img))
