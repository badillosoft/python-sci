# Objeto: Atributos y Metodos

class Persona:
    def __init__(self):
        self.nombre = "Anonimo"
        self.edad = 0
        self.sexo = "Indefinido"

    def saludar(self):
        print "Hola: %s" %(self.nombre)

p = Persona()

p.edad = 18

print "P: %s %d %s" %(p.nombre, p.edad, p.sexo)

q = Persona()

print "Q: %s %d %s" %(q.nombre, q.edad, q.sexo)