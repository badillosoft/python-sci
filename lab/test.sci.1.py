import sci

# CSV - Cargar una lista de diccionarios de un archivo csv

personas = sci.load_csv("datos_lab.csv")

#print personas

sexos = sci.data_extract(personas, "Sexo")

mujeres_checker = sci.data_checker(sexos, lambda sexo: sexo == "Mujer")

mujeres = sci.data_reduce(personas, mujeres_checker)

#print mujeres

ingresos_mujeres = sci.data_extract(mujeres, "Ingresos")

print ingresos_mujeres