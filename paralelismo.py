import multiprocessing

# Funcion que calcule el cuadrado de un número

def square(n):
    return n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    # Crear un pool de procesos
    with multiprocessing.Pool() as pool:
        # Mapear la función square a la lista de números
        results = pool.map(square, numbers)

    print("Squares:", results)
