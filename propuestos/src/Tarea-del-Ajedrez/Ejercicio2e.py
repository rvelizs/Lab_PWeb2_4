from interpreter import draw
from chessPictures import *

parte1 = square.negative().join(square)
parte2 = parte1.horizontalRepeat(4)

draw(Picture(parte2.img))