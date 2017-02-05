# 1. Abrir el archivo en modo lectura
archivo = open("datos_feos.csv", "r")

mat = []

# 2. Leer el archivo linea por linea
for linea in archivo:
    # 3. Cortar la cadena con el separador ","
    a = linea.split(",")
    
    # 4. Transformar los valores cortados
    # (numeros en forma de cadena) a numeros flotantes
    # el numero transformado lo guardamos en una nueva lista
    row = []
    for xs in a:
        try:
            x = float(xs)
        except:
            continue
        row.append(x)

    # 5. Agregar la fila a la matriz
    mat.append(row)

print mat

# x. cerrar el archivo
archivo.close()