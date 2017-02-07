import sci

# CSV - Cargar una lista de diccionarios de un archivo csv

personas = sci.load_csv("datos_lab.csv")

#print personas

def transform(persona):
	if persona["Sexo"] == "Mujer":
		return persona["Ingresos"]

ingresos_mujeres = sci.data_map(personas, transform)

print ingresos_mujeres