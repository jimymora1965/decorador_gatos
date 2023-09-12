class Felinos:
    def __init__(self, raza, origen):
        self._r = raza
        self._o = origen

    @property
    def raza(self):
        return self._r

    @property
    def origen(self):
        return self._o

    @raza.setter
    def raza(self, nueva_raza):
        self._r = nueva_raza

    @origen.setter
    def origen(self, nuevo_origen):
        self._o = nuevo_origen

print("\tCreamos un primer gato:")
gato = Felinos("Persa", "Medio Oriente\n")
gato_raza = gato.raza
origen = gato.origen
print(gato_raza)
print(origen)

print("\tCreamos un segundo gato:")

gato.raza = "Siames"
raza = gato.raza
print(raza)
gato.origen = "Siam\n"
origen = gato.origen
print(origen)

print("\tCreamos un tercer gato:")

gato.raza = "Criollo"
raza = gato.raza
print(raza)
gato.origen = "Colombia\n"
origen = gato.origen
print(origen)

print("\tCreamos un cuarto gato:")

gato.raza = "Angora"
raza = gato.raza
print(raza)
gato.origen = "Anatolia Turquia"
origen = gato.origen
print(origen
      )