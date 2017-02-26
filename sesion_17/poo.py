# Objeto: Atributos y Metodos

class Persona:
    def saludar(self):
        print "Hola: %s" %(self.nombre)

p = Persona()

p.nombre = "Pepe"

p.saludar()