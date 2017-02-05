# -*- coding: utf-8 -*-

personas = [{u'Edad': 23L, u'Nombre': u'Alberto', u'Peso': 123L, u'Sexo': u'Hombre'}, {u'Edad': 32L, u'Nombre': u'Bere', u'Peso': 32L, u'Sexo': u'Muejer'}, {u'Edad': 45L, u'Nombre': u'Carlos', u'Peso': 45L, u'Sexo': u'Hombre'}, {u'Edad': 54L, u'Nombre': u'Diana', u'Peso': 65L, u'Sexo': u'Muejer'}, {u'Edad': 67L, u'Nombre': u'Eduardo', u'Peso': 47L, u'Sexo': u'Hombre'}, {u'Edad': 76L, u'Nombre': u'Fatima', u'Peso': 78L, u'Sexo': u'Muejer'}]

personas_jovenes = []

for persona in personas:
    #if persona["Edad"] >= 30 and persona["Edad"] <= 50:
    if persona["Sexo"] == "Muejer":
        personas_jovenes.append(persona)

print personas_jovenes