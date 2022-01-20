
class Vehiculo:
    def __init__(self):
        self.asientos = 6

class Minibus(Vehiculo):
    def __init__(self):
        super().__init__(self)
        self.disponible = []

    def capacidad(self, cap):
        self.capacidad = cap

    def agregar(self, pasajero):
        if len(self.disponible) <= self.capacidad:
            if pasajero in self.disponible:
                print(f'{pasajero} ya esta dentro!')
            else:
                self.disponible.append(pasajero)
        else:
            print("Capacidad maxima")

    def lleno(self):
        return True if (self.capacidad > len(self.disponible)) else False


class Pasajero:
    def __init__(self, nombre):
        self.nombre = nombre


bus = Minibus()
bus.capacidad(5)

while bus.lleno():
    pasaj = Pasajero(input("Ingrese un pasajero: "))
    bus.agregar(pasaj.nombre)
    print(len(bus.disponible))