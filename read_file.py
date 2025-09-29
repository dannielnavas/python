# Leer un archivo línea por línea y mostrar su contenido
with open('cuento.txt', 'r') as file:
    for line in file:
        print(line.strip()) # Eliminar espacios en blanco alrededor de la línea


# Leer todas la lineas pero en una lista r hace referencia a read
with open('cuento.txt', 'r') as file:
    lines = file.readlines()
    print(lines)  # Muestra todas las líneas como una lista


# Leer y agregar contenido al final del archivo la a hace referencia a append
with open('cuento.txt', 'a') as file:
    file.write("\nY vivieron felices para siempre.")


# Sobrescribir el contenido del archivo w hace referencia a write
with open('cuento.txt', 'w') as file:
    file.write("Érase una vez un reino muy lejano...")
