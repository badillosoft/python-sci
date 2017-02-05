from sci import dic_xl

personas = dic_xl("Libro1.xlsx", "Hoja1", "C4:F10")

for persona in personas:
    print persona