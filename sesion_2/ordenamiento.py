def buscar_menor(lista):
    m = lista[0]
    im = 0
    n = len(lista)

    for i in range(0, n):
        if lista[i] < m:
            m = lista[i]
            im = i
    
    return im

lista = [8, 9, 1, 3, 2, 6]

lista2 = []

while len(lista) > 0:
    i = buscar_menor(lista)
    x = lista.pop(i)
    lista2.append(x)

print lista2