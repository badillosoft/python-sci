# Objeto: Atributos y Metodos

class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def saludar(self):
        print "Hola: %s" %(self.nombre)

p = Persona("Pepe", 18, "Hombre")

print "P: %s %d %s" %(p.nombre, p.edad, p.sexo)

q = Persona("Paco", 81, "Hombre")

print "P: %s %d %s" %(q.nombre, q.edad, q.sexo)

p.saludar()
q.saludar()