import requests
import matplotlib.pyplot as plt
import json

TOKEN = "3e4bac1e-07ad-2db4-44d4-fc13628338b2"

URL_API = "http://www3.inegi.org.mx/sistemas/api/indicadores/v1/Indicador"

for a in range(33):
	area = "0%d" % a if a < 10 else str(a)
	
	url_hombres = "%s/1002000002/%s/es/true/json/%s" % (URL_API, area, TOKEN)
	url_mujeres = "%s/1002000003/%s/es/true/json/%s" %(URL_API, area, TOKEN)
	
	json_hombres = json.loads(requests.get(url_hombres).content)
	json_mujeres = json.loads(requests.get(url_mujeres).content)
	
	total_hombres = json_hombres["Data"]["Serie"][0]["CurrentValue"]
	total_mujeres = json_mujeres["Data"]["Serie"][0]["CurrentValue"]
	
	labels = ['Hombres', 'Mujeres']
	sizes = [total_hombres, total_mujeres]
	
	fig, ax = plt.subplots()
	ax.pie(sizes, labels=labels, autopct='%1.1f%%',
		shadow=True, startangle=90)
	
	nombre_region = json_hombres["MetaData"]["Region"]
	nombre_archivo = "img_a1/%s. %s.png" % (area, nombre_region.replace(",", " - "))
	plt.savefig(nombre_archivo)
