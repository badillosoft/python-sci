import requests
import sci

html = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Mi Aplicacion</title>
    </head>
    <body>
        <table>
            <tr>
                <th>Nombre</th>
                <th>Edad</th>
                <th>Sexo</th>
            </tr>
            <tr>
                <th>Ana</th>
                <th>21</th>
                <th>Mujer</th>
            </tr>
            <tr>
                <th>Beto</th>
                <th>12</th>
                <th>Hombre</th>
            </tr>
            <tr>
                <th>Carla</th>
                <th>45</th>
                <th>Mujer</th>
            </tr>
    </body>
</html>
"""

tags = sci.html_tags(html)

import json

jtags = json.dumps(tags, sort_keys=True, indent=4)

print jtags