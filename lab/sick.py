from random import choice, random

def generar_nombres(nombres, apellidos, total):
	aux = []
	for i in range(total):
		nombre = choice(nombres)
		apellido = choice(apellidos)
		aux.append("%s %s" %(apellido, nombre))
	return aux

def modelo_enfermedad1(sintoma1, sintoma2, sintoma3):
	if sintoma1 == "SI":
		if sintoma2 == "SI":
			if sintoma3 == "SI":
				return "SI" if random() <= 0.8 else "NO"
			return "SI" if random() <= 0.7 else "NO"
		if sintoma3 == "SI":
			return "SI" if random() <= 0.6 else "NO"
		return "SI" if random() <= 0.5 else "NO"
	return "SI" if random() <= 0.2 else "NO"

def modelo_enfermedad2(sintoma1, sintoma2, sintoma3):
	if sintoma1 == "SI":
		if sintoma2 == "SI":
			if sintoma3 == "SI":
				return "SI" if random() <= 0.9 else "NO"
			return "SI" if random() <= 0.7 else "NO"
		if sintoma3 == "SI":
			return "SI" if random() <= 0.3 else "NO"
		return "SI" if random() <= 0.1 else "NO"
	return "SI" if random() <= 0.25 else "NO"

def modelo_sintoma1():
	return "SI" if random() <= 0.16 else "NO"

def modelo_sintoma2():
	return "SI" if random() <= 0.21 else "NO"

def modelo_sintoma3():
	return "SI" if random() <= 0.38 else "NO"

def matriz_enfermedades(nombres, apellidos, total):
	mat = [["Nombre", "Sintoma 1", "Sintoma 2", "Sintoma 3", "Enfermedad 1", "Enfermedad 2"]]
	for nombre in generar_nombres(nombres, apellidos, total):
		s1 = modelo_sintoma1()
		s2 = modelo_sintoma2()
		s3 = modelo_sintoma3()
		e1 = modelo_enfermedad1(s1, s2, s3)
		e2 = modelo_enfermedad2(s1, s2, s3)
		mat.append([nombre, s1, s2, s3, e1, e2])
	return mat

def lista_enfermedades(nombres, apellidos, total):
	lista = []
	for nombre in generar_nombres(nombres, apellidos, total):
		s1 = modelo_sintoma1()
		s2 = modelo_sintoma2()
		s3 = modelo_sintoma3()
		e1 = modelo_enfermedad1(s1, s2, s3)
		e2 = modelo_enfermedad2(s1, s2, s3)
		persona = {
			"Nombre": nombre,
			"Sintoma 1": s1,
			"Sintoma 2": s2,
			"Sintoma 3": s3,
			"Enfermedad 1": e1,
			"Enfermedad 2": e2
		}
		lista.append(persona)
	return lista
