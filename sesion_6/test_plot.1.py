from sci import load_xl, data_map, data_filter

datos = load_xl("Libro1.xlsx", "Datos", "A1:D102")

def es_hombre(dic):
    if dic["Sexo"] == "Hombre":
        return True

def es_mujer(dic):
    if dic["Sexo"] == "Mujer":
        return True

def es_otro(dic):
    if dic["Sexo"] == "Indefinido":
        return True

hombres = data_filter(datos, es_hombre)
mujeres = data_filter(datos, es_mujer)
otros = data_filter(datos, es_otro)

H = len(hombres)
M = len(mujeres)
O = len(otros)

import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = ['Hombre', 'Mujer', "Indefinido"]
sizes = [H, M, O]
explode = [0, 0, 0.4]  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()