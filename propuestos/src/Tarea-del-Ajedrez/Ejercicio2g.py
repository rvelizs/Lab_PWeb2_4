from interpreter import draw
from chessPictures import *

torre1 = rock.up(square)
caballo1 = knight.up(square.negative())
alfil1 = bishop.up(square)
reina = queen.up(square.negative())
rey = king.up(square)
alfil2 = bishop.up(square.negative())
caballo2 = knight.up(square)
torre2 = rock.up(square.negative())

