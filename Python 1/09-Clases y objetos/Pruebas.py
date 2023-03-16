class Coche:
    def __init__(self, marca, modelo, combustible, año, kmh, cv):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.año = año
        self.kmh = kmh
        self.cv = cv



    def consumo_coche(self):
        return self.kmh / self.cv


marca = input('Marca:')
modelo = input('Modelo:')
combustible = input('Combustible:')
año = int(input('Año:'))
kmh = int(input('Kmh:'))
cv = int(input('Cv:'))

coche1 = Coche(marca, modelo, combustible, año, kmh, cv)
print(coche1.consumo_coche())
