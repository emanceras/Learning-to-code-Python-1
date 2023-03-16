class Rectangulo:
    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base


altura = int(input("Altura:"))
base = int(input("Base:"))

rectangulo1 = Rectangulo(altura, base)
print(f'Área de rectángulo es: {rectangulo1.calcular_area()}')
