import sci

# CSV - Cargar una lista de diccionarios de un archivo csv

personas = sci.load_csv("datos_lab.csv")

#print personas

mujeres = sci.data_filter(personas, lambda persona: persona["Sexo"] == "Mujer")

#print mujeres

ingresos_mujeres = sci.data_extract(mujeres, "Ingresos")

print ingresos_mujeres