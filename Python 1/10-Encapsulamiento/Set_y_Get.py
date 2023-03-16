# Para hacer un atributo privado se pone una '_' entre el punto y el nombre del atributo.
class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def print(self):
        print(f'Nombre = {self._nombre}, Apellido = {self._apellido}, edad = {self._edad}')


persona1 = Persona('Juan', 'González', 25)
persona1.print()


# GET Y SET
class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property  # Este es el GET
    def nombre(self):
        return self._nombre

    @nombre.setter  # Este es el SET, es obligatorio que el SET vaya debajo del GET
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def print(self):
        print(f'Nombre = {self._nombre}, Apellido = {self._apellido}, edad = {self._edad}')


persona2 = Persona('Juan', 'González', 25)
persona2.nombre = 'Juan Carlos'
print(persona2.nombre)
