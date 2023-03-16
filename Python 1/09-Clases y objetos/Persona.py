class Persona:
    def __init__(self):
        self.nombre = 'Juan'
        self.apellido = 'Gonzalez'
        self.edad = 28


persona1 = Persona()
print(persona1.nombre)


########################
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


persona2 = Persona('Manuel', 'Perez', 32)
print(f'Nombre: {persona2.nombre}, Apellido: {persona2.apellido}, Edad: {persona2.edad}')
# Modificar un atributo
persona2.nombre = 'Jose Manuel'
print(persona2.nombre)


# Crear método para imprimir desde la clase
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def imprimir(self):
        print(f'Cliente: {self.nombre} {self.apellido}, {self.edad}')


persona2 = Persona('Manuel', 'Perez', 32)
persona2.imprimir()
