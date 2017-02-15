from flask import Flask, make_response

import StringIO

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg

app = Flask(__name__)

@app.route("/graficas/f1")
def foo():
    X = [1, 2, 3, 4, 5]
    Y = [1, 4, 9, 16, 25]
    
    fig, ax = plt.subplots()

    ax.plot(X, Y)

    canvas = FigureCanvasAgg(fig)

    png_output = StringIO.StringIO()

    canvas.print_png(png_output)

    response = make_response(png_output.getvalue())

    response.headers["Content-Type"] = "image/png"

    return response

app.run(host="localhost", port=3000)