import sci

datos = sci.load_xl("sintomas.xlsx", "Hoja1", "B3:G8")

def tdatoX(paciente):
    sexo = 1 if paciente["Sexo"] == "Hombre" else 2

    s1 = 1 if paciente["S1"] == "SI" else 0
    s2 = 1 if paciente["S2"] == "SI" else 0
    s3 = 1 if paciente["S3"] == "SI" else 0

    return [sexo, s1, s2, s3]

def tdatoY(paciente):
    e1 = 1 if paciente["E1"] == "SI" else 0
    e2 = 1 if paciente["E2"] == "SI" else 0

    return [e1, e2]

X = sci.data_map(datos, tdatoX)
Y = sci.data_map(datos, tdatoY)

print "ok"

from sklearn.neural_network import MLPClassifier

clr = MLPClassifier()

clr.fit(X, Y)

print clf.predict([[1, 1, 0, 1]])