from sick import lista_enfermedades
from sci import data_build, write_sheet_xl
from openpyxl import load_workbook

nombres = [
	"Ana", "Alberto", "Bere", "Beto", "Carla", "Carlos",
	"Daniela", "Daniel", "Eduardo", "Eli", "Fabian", "Fany",
	"Gera", "Gaby", "Hugo", "Helen", "Juan", "Jaz",
	"Karen", "Krilin", "Mauro", "Maria", "Nico", "Nadia",
	"Orlando", "Olga", "Paco", "Paty", "Raul", "Rosa"
]

apellidos = [
	"Alvarez", "Benitez", "Camacho", "Dante",
	"Escamilla", "Fernandez", "Gonzalez", "Hernandez",
	"Jimenez", "Lugo", "Martinez", "Oropeza", "Piedras"
]

enfermedades = lista_enfermedades(nombres, apellidos, 100)

labels = ["Nombre", "Sintoma 1", "Sintoma 2", "Sintoma 3", "Enfermedad 1", "Enfermedad 2"]

write_xl("Libro1.xlsx", "Enfermedades", "A1", enfermedades, labels)