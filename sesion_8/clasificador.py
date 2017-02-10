from sklearn.neural_network import MLPClassifier
import sci

datos = sci.load_xl("sintomas.xlsx", "Hoja1", "B3:G8")

def tsexo(paciente):
    if paciente["Sexo"] == "Hombre":
        return 1
    return 2

def tsino(paciente):
    if paciente[k] == "SI":
        return 1
    return 0

sexos = sci.data_map(datos, tsexo)

k = "S1"
s1 = sci.data_map(datos, tsino)

k = "S2"
s2 = sci.data_map(datos, tsino)

k = "S3"
s3 = sci.data_map(datos, tsino)

k = "E1"
e1 = sci.data_map(datos, tsino)

k = "E2"
e2 = sci.data_map(datos, tsino)




