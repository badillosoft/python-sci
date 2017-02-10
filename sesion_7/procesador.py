from sci import load_xl, data_map

datos = load_xl("datos_flujo.xlsx", "Hoja1", "B2:D9")

def f(dic):
    # dic (N, S, A)
    if dic["S"] > 5:
        return dic

filtrados = data_map(datos, f)

print filtrados