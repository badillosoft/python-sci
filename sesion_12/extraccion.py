import requests

page = requests.get("http://cuentame.inegi.org.mx/monografias/informacion/gro/default.aspx?tema=me&e=12")

print page.content

f = open("output.html", "w")

f.write(page.content)

f.close()