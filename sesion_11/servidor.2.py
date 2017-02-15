from flask import Flask, make_response

import StringIO

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

import sci

app = Flask(__name__)

@app.route("/graficas/f1")
def foo():
    # Cargamos los datos
    datos1 = sci.load_xl("Libro1.xlsx", "Hoja1", "D4:D10")
    datos2 = sci.load_xl("Libro1.xlsx", "Hoja1", "E4:E10")

    w = 0.8 / 2

    x1 = [1, 2, 3, 4]
    x2 = [1 + w, 2 + w, 3 + w, 4 + w]

    c0_20_1 = len(sci.data_filter(datos1, lambda dic: dic["Edad"] <= 20))
    c21_40_1 = len(sci.data_filter(datos1, lambda dic: dic["Edad"] > 20 and dic["Edad"] <= 40))
    c41_60_1 = len(sci.data_filter(datos1, lambda dic: dic["Edad"] > 40 and dic["Edad"] <= 60))
    c61_x_1 = len(sci.data_filter(datos1, lambda dic: dic["Edad"] > 60))
    
    c0_20_2 = len(sci.data_filter(datos2, lambda dic: dic["Edad"] <= 20))
    c21_40_2 = len(sci.data_filter(datos2, lambda dic: dic["Edad"] > 20 and dic["Edad"] <= 40))
    c41_60_2 = len(sci.data_filter(datos2, lambda dic: dic["Edad"] > 40 and dic["Edad"] <= 60))
    c61_x_2 = len(sci.data_filter(datos2, lambda dic: dic["Edad"] > 60))

    y1 = [c0_20_1, c21_40_1, c41_60_1, c61_x_1]
    y2 = [c0_20_2, c21_40_2, c41_60_2, c61_x_2]

    fig, ax = plt.subplots()

    ax.bar(x1, y1, w) #
    ax.bar(x2, y2, w) #

    # Regresamos la imagen como la respuesta del servidor
    canvas = FigureCanvasAgg(fig)

    png_output = StringIO.StringIO()

    canvas.print_png(png_output)

    response = make_response(png_output.getvalue())

    response.headers["Content-Type"] = "image/png"

    return response

app.run(host="localhost", port=3000)