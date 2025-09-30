import os

cwd = os.getcwd()
print("Current working directory:", cwd)

# Listar  archivos y directorios en el directorio actual
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print("Text files in the current directory:", txt_files)


os.rename('cuento.txt', 'nuevo_cuento.txt')
print("File renamed from 'cuento.txt' to 'nuevo_cuento.txt'")
