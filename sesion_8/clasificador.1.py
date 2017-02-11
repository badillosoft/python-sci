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

from sklearn.neural_network import MLPClassifier

clf = MLPClassifier()

clf.fit(X, Y)

Yp = clf.predict([[1, 1, 0, 1], [0, 0, 0, 1]])

def f(Y):
    return {
        "E1": "SI" if Y[0] == 1 else "NO",
        "E2": "SI" if Y[1] == 1 else "NO"
    }

Ys = sci.data_map(Yp, f)

print Ys