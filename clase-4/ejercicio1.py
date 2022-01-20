# Escribe una clase de Python llamada Rectangulo que se define por una longitud y un ancho y un método que calculará el área de un rectángulo

class Rectangulo:
    def __init__(self, long, ancho):
        self.long = long
        self.ancho = ancho

    def area(self):
        return f"El area es {self.long * self.ancho}"

rec = Rectangulo(2,5)
print(rec.area())