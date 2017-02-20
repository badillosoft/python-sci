import requests

data = requests.get("http://www3.inegi.org.mx/sistemas/api/indicadores/v1/Indicador/1002000001/01/es/false/json/TOKEN")

print data.content