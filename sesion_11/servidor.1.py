from flask import Flask, make_response

import StringIO

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

import sci

app = Flask(__name__)

@app.route("/graficas/f1")
def foo():
    # Cargamos los datos
    datos = sci.load_xl("Libro1.xlsx", "Hoja1", "E4:E10")

    # Cargamos las categorias de Sexo
    categorias = sci.cat_set_build(datos, ["Sexo"])[0]

    # Calculamos los totales
    total = {}

    for cat in categorias:
        total[cat] = len(sci.data_filter(datos,
            lambda dic: dic["Sexo"] == cat))

    # Calculamos los totales por categoria
    sizes = [total[cat] for cat in categorias]
    labels = categorias

    # Dibujamos el pastel
    fig, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    # Regresamos la imagen como la respuesta del servidor
    canvas = FigureCanvasAgg(fig)

    png_output = StringIO.StringIO()

    canvas.print_png(png_output)

    response = make_response(png_output.getvalue())

    response.headers["Content-Type"] = "image/png"

    return response

app.run(host="localhost", port=3000)