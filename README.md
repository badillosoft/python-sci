# Python SCI

Instructor: Alan Badillo Salas <badillo.soft@hotmail.com>

## Proyectos

### Extracción de datos del Ingegi.

El Instituto Nacional de Estadística y Geografía (INEGI) posee un
API del Banco de Indicadores. Para utilizarlo es necesario
obtener un token ingresando a está página:
[http://www.beta.inegi.org.mx/servicios/api_biinegi.html](http://www.beta.inegi.org.mx/servicios/api_biinegi.html)

> En la sección de **Guía para desarrolladores** busque dónde dice `token`.

Una vez obtenido el token por correo electrónico vaya a la sección de
**Ejemplo** para ver como se construye una url similar a esta:
[http://www3.inegi.org.mx/sistemas/api/indicadores/v1/Indicador/1002000001/01/es/false/json/](http://www3.inegi.org.mx/sistemas/api/indicadores/v1/Indicador/1002000001/01/es/false/json/)

Extraíga los datos desde *python* analizando el siguiente ejemplo:

~~~py
import requests

data = requests.get("http://www3.inegi.org.mx/sistemas/api/indicadores/v1/Indicador/1002000001/01/es/false/json/TOKEN")

print data.content
~~~

### Proyecto A1 - Análisis de población 1

* Construye las url para los indicadores `1002000002` (población total de hombres) y
`1002000003` (población total de mujeres) de las áreas geográficas `00` (Todo el país)
hasta la `32` (Zacatecas) y datos más recientes `true`.

Para cada entidad se obtendrá un *json* similar a este:

~~~json
{
	"Data": {
		"GeneralNote": "Esta información se actualiza cada cinco años mediante los Censos y Conteos de población y vivienda.",
		"GeneralSource": null,
		"Serie": [
			{
				"CurrentValue": "1563460",
				"DescriptionPeriod": "2010",
				"NotesPeriod": "Incluye a la población estimada, la cual corresponde a las viviendas sin información de ocupantes.La información es censal y está referida al 12 de junio de 2010.",
				"SourcesPeriod": "INEGI Censo de Población y Vivienda 2010.",
				"TimePeriod": "2010",
				"ValueStatus": "Definitiva"
			}
		]
	},
	"MetaData": {
		"CreationDate": "20/02/2017 01:00:10 p. m.",
		"Freq": "Quinquenal",
		"Indicator": 1002000003,
		"LastUpdate": "",
		"Name": "Población total mujeres",
		"NoOfDecimals": "0",
		"Unit": "Número de personas",
		"Region": "Baja California,Estatal"
	}
}
~~~

Por cada área geográfica construye una gráfica de pastel entre la población total de hombres
y la población total de mujeres. Guarda la gráfica mediante `plt.savefig()` con
el nombre de archivo construido a partir del área geográfica y nombre de la región,
ten en cuenta que la `,` se deberá reemplazar por ` - `.
Observa que en `MetaData>Region` se encuentra el nombre de la región.
El formato será similar a este:

~~~py
...
# area <- "02"
# nombre <- "Baja California,Estatal".replace(",", " - ")
plt.savefig("%s. %s.png" % (area, nombre))
...
~~~

Pseudo-código:

~~~py
# Importar requestsmatplotlib
# definir TOKEN = "..."
# definir URL_API = "http://www3.inegi.org.mx/sistemas/api/indicadores/v1/Indicador"
# Para cada area en ["00" hasta "32"]:
# 	url_hombres = "%s/1002000002/%s/es/true/json/%s" %(URL_API, area, TOKEN)
# 	url_mujeres = "%s/1002000003/%s/es/true/json/%s" %(URL_API, area, TOKEN)
#	Obtener `json_hombres` de url_hombres mediante requests
#	Obtener `json_mujeres` de url_mujeres mediante requests
#	Obtener `total_hombres` de json_hombres>Data>Serie>CurrentValue
#	Obtener `total_mujeres` de json_mujeres>Data>Serie>CurrentValue
#	Construir una gráfica de pastel que represente el total de hombres y mujeres
#	> tome en cuenta los sizes y labels (ver sesion_6>test_plot.1.py)
#	Obtener `nombre_region` de json_hombres>MetaData>Region
#	nombre_archivo = "%s. %s.png" % (area, nombre_region.replace(",", " - "))
#	Guardar la gráfica en el archivo nombre_archivo
~~~

### Proyecto A2 - Análisis de población 2

Basado en el `Proyecto 1` se requiere un sistema que genere histogramas por área geográficas
con las siguientes propiedades:

* Cada histograma tomará los datos de los indicadores
`1002000002` (población total de hombres) y `1002000003` (población total de mujeres).

* Se deberán cargar todos los datos por lo que *datos más recientes* tendrá `false`.

* En el eje de las `x` del histograma se deberán mostrar los años extraídos
de `Data>Serie>TimePeriod`.

* En cada `TimePeriod` habrán dos barras: una azul con la población total de hombres
y otra rosa para la población total de mujeres.

* El título de la gráfica se construirá a partir del área geográfica y la región.

* En la gráfica se deberá mostrar una leyenda que muestre que azul es la población total
de hombres y rosa la población total de mujeres.

* Las gráficas se guardarán como en el `Proyecto 1` pero con `hist` antes de `.png`.

### Proyecto B1 - Mapa de riqueza 1

El indicador `6200240329` (ingreso corriente total promedio trimestral por hogar)
y `6200240360` (Gasto corriente total promedio trimestral por hogar)
nos ayudarán a construir un indicador llamado nivel de riqueza de la
siguiente forma: Si `I` es el ingreso y `G` el gasto entonces `R = (2 * I - G) / (I + G)`
nos indican cual es el nivel de ingreso corriente total promedio trimestral por hogar
retenido después del gasto, es decir el nivel de riqueza.

* Construye un excel que contenga las 32 entidades con los datos de las
siguientes columnas y rellena los datos manualmente o mediante el API del INEGI.

> Entidad - El nombre de la entidad, ejemplo, `Hidalgo`

> Area - Área geográfica del INEGI para la entidad, ejemplo, `02`

> Capital - La capital del estado, ejemplo, `Pachuca de Soto`

> Latitud - Latitud de la capital del estado, ejemplo, `20.0825159`

> Longitud - Longitud de la capital del estado, ejemplo, `-98.7917974`

> Ingresos - El indicador `6200240329`

> Gastos - El indicador `6200240360`

> Riqueza - El indicador construido `R = (2 * I - G) / (I + G)`

### Proyecto B2 - Mapa de riqueza 2

* Obtener el mínimo de riqueza y el máximo del indicador de riqueza
y guardarlos en dos celdas que desee.

* Crear un cuarto indicador llamado `Color` el cual contendrá
un color según `int(3 * (R - MIN) / (MAX - MIN))`: `0 - Rojo`, `1 - Naranja`,
`2 - Amarillo`, `3 - Verde`.

* Tomar cada entidad del excel para pintar un punto centrado en la latitud y longitud
de la capital de cada entidad y colorear el punto según el color de su indicador de
riqueza.

* Guardar la gráfica en una imagen.

## Tareas

### Tarea 1

Crear un archivo llamado `datos_tarea1.csv` el cual contenga los
siguientes datos:

~~~csv
Nombre, Sexo, Ingresos, Gastos
Ana, Mujer, 12500, 9700
Beto, Hombre, 8900, 6800
Carla, Mujer, 10300, 4300
Daniel, Hombre, 9400, 6200
Estefany, Mujer, 11700, 10300
Fabian, Hombre, 9200, 6500
Gloria, Mujer, 8500, 7200
Hugo, Hombre, 10200, 8100
Ilse, Mujer, 12100, 9200
Juan, Hombre, 12300, 11200
Maria, Mujer, 11900, 3200
Nicolas, Hombre, 10800, 5500
Paty, Mujer, 9600, 9200
Raul, Hombre, 8900, 4800
~~~

Crer un programa que tome los datos del archivo `csv` y los
transforme a una matriz y posteriormente a una lista de diccionarios.

Crear un programa que encuentre a la persona con mayor ingresos
y a la persona con mayores gastos.

## Ejecicios

### Ejercicio 1

Crear un archivo de excel con el siguiente formato:

> Excel - Hoja 1 B4:D8

~~~xlsx
Nombre	Ingresos	Gastos
Ana	17200		6800
Beto	15300		9500
Carla	12600		7600
Daniel	15400		3400
~~~

> Excel - Hoja 1 B11:D15

~~~xlsx
Nombre	Ingresos	Gastos
Ana	16400		7900
Beto	17800		8400
Carla	14300		5600
Daniel	15900		3600
~~~

> Excel - Hoja 1 B19:D22

~~~xlsx
Nombre	Ingresos	Gastos
Ana	12300		9200
Beto	18500		7900
Carla	19200		10300
Daniel	13600		7800
~~~

Leer los datos en listas de diccionarios llamados `enero`, `febrero` y `marzo`
que contengan los datos de cada persona para el periodo indicado.

> Python - Ejemplo

~~~py
enero = [
	{
		"Nombre": "Ana",
		"Ingresos": 17200,
		"Gastos": 6800
	},
	{
		"Nombre": "Beto",
		"Ingresos": 15300,
		"Gastos": 9500
	},
	...
]

febrero = [
	{
		"Nombre": "Ana",
		"Ingresos": 16400,
		"Gastos": 7900
	},
	{
		"Nombre": "Beto",
		"Ingresos": 17800,
		"Gastos": 8400
	},
	...
]

...
~~~

Crear una lista de diccionarios llamado `total` que contenga
los datos para cada persona de *Nombre*, *Ingresos* y *Gastos*
sumando el total de ingresos para los meses *enero*, *febrero* y *marzo*.

> Python - Ejemplo

~~~py
total = [
	{
		"Nombre": "Ana",
		"Ingresos": 45900,
		"Gastos": 23900
	},
	{
		"Nombre": "Beto",
		"Ingresos": 51600,
		"Gastos": 25800
	},
	...
]
~~~

Solución: [youtube.com/watch?v=z21ldstYW1E](https://www.youtube.com/watch?v=z21ldstYW1E)

## Notas del curso