import sci

filename = "sintomas.xlsx"
sheet_name = "Hoja1"
cell_range = "B3:G8"

xlabels = ["Sexo", "S1", "S2", "S3"]
ylabels = ["E1", "E2"]

tests = [
    [0, 0, 0, 0]
]

###############################################################

# 1. Cargar los datos de analisis desde excel
datos = sci.load_xl(filename, sheet_name, cell_range)

# 2. recuperar las matrices de analisis
X, Y = sci.data_analize(datos, xlabels, ylabels)

# 3. Detectar las categorias automaticamente
xcats = sci.cat_set_build(datos, xlabels)
ycats = sci.cat_set_build(datos, ylabels)

print "Categorias X: %s" %str(xcats)
print "Categorias Y: %s" %str(ycats)

# 4. Transformar los datos por categoria
Xp = sci.cat_transform(X, xcats)
Yp = sci.cat_transform(Y, ycats)

print Xp

# 5. Aplicamos el clasificador para predecir nuevos datos
#from sklearn.neural_network import MLPClassifier

#clf = MLPClassifier()

#clf.fit(Xp, Yp)

#print clf.predict(tests)

from sklearn import linear_model

reg = linear_model.LinearRegression()
reg.fit (X, Y)

LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False