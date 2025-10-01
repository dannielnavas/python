x = 5

def modify_global():
    global x  # Declarar que usaremos la variable global 'x'
    x = 10    # Modificar la variable global
    print("Inside function, modified global x:", x)

modify_global()
print("Outside function, global x:", x)  # Imprime 10, ya que fue modificada dentro de la función
