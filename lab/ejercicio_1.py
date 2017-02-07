from sci import load_xl

enero = load_xl("ejercicio_1.xlsx", "Hoja 1", "B4:D8")
febrero = load_xl("ejercicio_1.xlsx", "Hoja 1", "B11:D15")
marzo = load_xl("ejercicio_1.xlsx", "Hoja 1", "B18:D22")

def ingresos(lista, nombre):
	for persona in lista:
		# persona (Nombre, Ingresos, Gastos)
		if persona["Nombre"] == nombre:
			return persona["Ingresos"]

def gastos(lista, nombre):
	for persona in lista:
		# persona (Nombre, Ingresos, Gastos)
		if persona["Nombre"] == nombre:
			return persona["Gastos"]

def nombres(lista):
	aux = []
	for persona in lista:
		aux.append(persona["Nombre"])
	return aux

total = []

for nombre in nombres(enero):
	persona = {
		"Nombre": nombre
	}

	s = 0
	for mes in [enero, febrero, marzo]:
		s += ingresos(mes, nombre)

	persona["Ingresos"] = s

	s = 0
	for mes in [enero, febrero, marzo]:
		s += gastos(mes, nombre)

	persona["Gastos"] = s

	total.append(persona)

print total
