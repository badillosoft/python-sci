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
        <div>
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
        </table>
    </body>
</html>
"""

# 1. Cargar las etiquetas del contenido html
tags = sci.html_tags(html)

# 2. Estructurar un arbol con las etiquetas
tree = sci.html_tree(tags)

# Buscar el nodo de la etiqueta table
table = sci.html_tree_search(tree, "table")

doc = tree["children"][0]
html = tree["children"][1]
head = html["children"][0]
body = html["children"][1]
table = body["children"][0]

# Estructurar la matriz del nodo
mat = []

for tr in table["children"]:
    row = []
    for th in tr["children"]:
        row.append(th["close_tag"]["text"])
    mat.append(row)

print mat