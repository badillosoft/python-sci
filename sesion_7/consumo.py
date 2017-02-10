from sci import load_xl, data_map
from datetime import datetime

clientes = load_xl("clientes.xlsx", "Hoja1", "A1:C1001")

def enero_2015(cliente):
    # cliente (Nombre, Fecha, Consumo)
    fecha = datetime.strptime(cliente["Fecha"], "%d-%m-%Y")
    ini = datetime.strptime("1-1-2015", "%d-%m-%Y")
    fin = datetime.strptime("31-1-2015", "%d-%m-%Y")

    if fecha >= ini and fecha <= fin:
        return cliente["Consumo"]

consumos = data_map(clientes, enero_2015)

total = sum(consumos)
promedio = total / len(consumos)

print "Total de consumo: %d Promedio: %.2f" %(total, promedio)

