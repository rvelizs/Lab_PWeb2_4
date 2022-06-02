from mimetypes import init
from colors import *
from pieces import *
class Picture:
  def __init__(self, img):
    self.img = img;
  
  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    aux = ""
    image = []
    for i in range(0, len(self.img)):
      for j in range(0, len(self.img[i])):
        aux = self.img[i][j] + aux
      image.append(aux)
      aux = ""
    
    return Picture(image)

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    
    aux = ""
    image = []
    for i in range(0, len(self.img)):
      for j in range(0, len(self.img[i])):
        
        
    
    
    
    for i in range (len(self.img)-1,):
      aux.append(self.img[::-1])
    
      print(aux[i])
    #self.img = aux
    #return Picture(aux)
  
  def negative(self):
    """ Devuelve un negativo de la imagen """
    #return Picture(None)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento al lado derecho de la figura actual """
    
    #return Picture(None)

  def up(self, p):
    """Hola"""
    #return Picture(None)
  
  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la figura actual """
    #return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado la cantidad de veces que indique el valor de n """
    #return Picture(None)

  def verticalRepeat(self, n):
    """Hola"""
    #return Picture(None)

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario o antihorario"""
    #return Picture(None)

