from interpreter import draw
from chessPictures import *

fil1 = knight.join(knight.negative())
fil2 = fil1.verticalMirror()
dibFinal = Picture(fil1.img + fil2.img)

draw(dibFinal)