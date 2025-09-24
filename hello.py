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

# your_name = input("¿Cuál es tu nombre? ")
# print("Hola " + your_name)
# your_age = int(input("¿Cuántos años tienes? "))
# print("Tienes " + str(your_age) + " años")

# Listas
todo = ["Aprender Python", "Hacer un proyecto", "Conseguir un trabajo"]
print(todo)
print(type(todo))
print(len(todo))
print(todo[0])
print(todo[1])
print(todo[0:1])

# Listas pueden tener diferentes tipos de datos
numbers = [1,2,3,4,'cinco',6.0]
print(numbers)
print(type(numbers))

string = 'Hola soy una cadena'
print(string[1:5])

# Listas pueden ser modificadas
new_list = [1,2,3,4,5, 'seis', 7.0, True, [8,9,10]]
new_list.append('once')
print(new_list)
new_list.insert(0, 'cero')
print(new_list)
print(new_list.index(3))

numbers_list = [1,2,3,4,5, 6,7,8,9,10]
print(max(numbers_list))
print(min(numbers_list))
print(sum(numbers_list))
print(numbers_list)
del numbers_list[0]
print(numbers_list)
del numbers_list[2:4]
print(numbers_list)
# del numbers_list
# print(numbers_list)  # Esto generará un error porque la lista ha sido eliminada


list_a = [1,2,3]
list_b = list_a
print(list_a)
print(list_b)
del list_a[0]
print(list_b)  # list_b aún existe porque es una referencia a la lista original
# print(list_a)  # Esto generará un error porque list_a ha sido eliminada
print(id(list_a))
print(id(list_b))

list_c = list_a[:]
print(list_c)
print(id(list_c))
print(id(list_a))
print(id(list_b))

list_a.append(4)
print(list_c)
print(list_a)
print(list_b)
