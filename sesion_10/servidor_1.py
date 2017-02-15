from flask import Flask
import sci
import json

app = Flask(__name__)

@app.route("/")
def home():
    datos = sci.load_xl("Libro1.xlsx", "Hoja1", "C4:F10")

    labels = sci.data_map(datos[0], lambda k: k)
    
    html = "<table>"

    html += "<tr>"
    for label in labels:
        html += "<th>%s</th>" % label
    html += "</tr>"

    for dic in datos:
        html += "<tr>"
        for label in labels:
            html += "<td>%s</td>" % (str(dic[label]))
        html += "</tr>"

    html += "</table>"

    return html

@app.route("/datos/<nombre>/<hoja>/<rango>")
def datos(nombre, hoja, rango):
    data = sci.load_xl("%s.xlsx"%nombre, hoja, rango)
    return json.dumps(data)

app.run(host="127.0.0.1", port=3000)