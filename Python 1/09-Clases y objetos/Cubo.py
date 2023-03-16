class Cubo:
    def __init__(self, ancho, alto, largo):
        self.ancho = ancho
        self.alto = alto
        self.largo = largo

    def calcular_volumen(self):
        return self.ancho * self.alto * self.largo


ancho = int(input('Introduce el ancho:'))
alto = int(input('Introduce el alto:'))
largo = int(input('Introduce el largo:'))

cubo1 = Cubo(ancho, alto, largo)
print(cubo1.calcular_volumen())
