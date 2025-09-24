print("Hello world")
print(1 + 1)

saludo = "Hola"
nombre = "Daniel"
print(saludo)
print(nombre)


name = "Daniel"
caracter = "c"
print(type(name))
print(type(caracter))

new_name = 'Daniel'
print(new_name)
print(type(new_name))

other_name = '''Daniel
Navas'''
print(other_name)
print(type(other_name))


indexacion = 'Danniel'
last_name = 'Navas'
# indexacion de cadenas
print(indexacion[0])
print(indexacion[1])
print(indexacion[2])
print(indexacion[3])
print(indexacion[4])
print(indexacion[-2])

# concatenacion de cadenas
print(indexacion + ' ' + last_name)
# repite la cadena n veces
print(indexacion * 3)
print(indexacion + ' ' + last_name * 3)
# obtiene la longitud de la cadena
print(len(indexacion))
print(len(last_name))

upperCaseName = 'DANNIEL'
# convierte a minusculas
print(upperCaseName.lower())
lowerCaseName = 'danniel'
# convierte a mayusculas
print(lowerCaseName.upper())

space_name = '   danniel    '
# elimina los espacios en blanco al inicio y al final
print(space_name.strip())
