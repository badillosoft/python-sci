from flask import Flask, make_response

import StringIO

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

import sci

app = Flask(__name__)

@app.route("/graficas/f1")
def foo():
    # Cargamos los datos
    datos = sci.load_csv("serie.csv")

    x = sci.data_map(datos, lambda dic: dic["tiempo"])
    y1 = sci.data_map(datos, lambda dic: dic["sensor1"])
    y2 = sci.data_map(datos, lambda dic: dic["sensor2"])
    y3 = sci.data_map(datos, lambda dic: dic["sensor3"])

    fig, ax = plt.subplots()

    ax.plot(x, y1)
    ax.plot(x, y2)
    ax.plot(x, y3)

    # Regresamos la imagen como la respuesta del servidor
    canvas = FigureCanvasAgg(fig)

    png_output = StringIO.StringIO()

    canvas.print_png(png_output)

    response = make_response(png_output.getvalue())

    response.headers["Content-Type"] = "image/png"

    return response

app.run(host="localhost", port=3000)