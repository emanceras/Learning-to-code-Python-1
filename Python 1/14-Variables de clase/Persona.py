class Persona:
    contador_personas = 0

    def __init__(self, nombre, edad):
        Persona.contador_personas += 1
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} { self.edad}]'


persona1 = Persona('Pepe', 42)
print(persona1)
persona2 = Persona('Carla', 23)
print(persona2)


#####################################################################
class Persona:
    contador_personas = 0

    @classmethod
    def generar_siguiente_persona(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        self.id_persona = Persona.generar_siguiente_persona()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} { self.edad}]'


persona1 = Persona('Pepe', 42)
print(persona1)
persona2 = Persona('Carla', 23)
print(persona2)