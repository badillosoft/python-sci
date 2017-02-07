# Python SCI

Instructor: Alan Badillo Salas <badillo.soft@hotmail.com>

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