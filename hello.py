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


x = 10
# tipo de dato int
print(type(x))
y = 3.534
# tipo de dato float
print(type(y))
# Notación científica para datos muy grandes o muy pequeños
z = 1.2e6
print(type(z))
# Notación científica para datos muy grandes o muy pequeños
a = 2.e-4
print(type(a))

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)  # división entera
print(x % y)   # módulo
print(x ** 2)  # potencia
print(x ** 3)  # potencia
print(pow(x, 3))  # potencia
print(round(y))  # redondeo
print(abs(-4.5))  # valor absoluto
print(abs(4.5))  # valor absoluto

is_true = True
print(type(is_true))
is_false = False
print(type(is_false))

#operadores numericos
aa = 10
bb = 20

print(aa + bb)
print(aa - bb)
print(aa * bb)
print(aa / bb)

aa += 2
print(aa)
aa -= 2
print(aa)
aa *= 2
print(aa)
aa /= 2
print(aa)

# precedencia de operadores
operacion_1 = 2 + 3 * 5
print(operacion_1)

# uso de paréntesis
operacion_2 = (2 + 3) * 5
print(operacion_2)

# uso de exponentes
operacion_3 = 2 + 3 * 5 ** 2
print(operacion_3)

# combinación de paréntesis y exponentes
operacion_4 = (2 + 3 * 5) ** 2
print(operacion_4)

# mayor que
print(aa > bb)
# menor que
print(aa < bb)
# mayor o igual que
print(aa >= bb)
# menor o igual que
print(aa <= bb)
# igual que
print(aa == bb)
# diferente que
print(aa != bb)
