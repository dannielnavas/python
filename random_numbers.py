import random

# Generar un numero entero aleatorio entre 1 y 10
random_number = random.randint(1, 10)
print("Random integer between 1 and 10:", random_number)

# Elegir colores aleatoriamente de una lista
colors = ['red', 'blue', 'green', 'yellow', 'purple']
random_color = random.choice(colors)
print("Random color chosen:", random_color)

# Barajar una lista de cartas
cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
random.shuffle(cards)
print("Shuffled cards:", cards)
