def outer_function():
    x = 'Outer'

    def inner_function():
        nonlocal x  # Declarar que usaremos la variable 'x' del ámbito externo (outer_function)
        x = 'Inner'
        print("Inner:", x)  # Imprime 'Inner'

    inner_function()
    print("Outer:", x)      # Imprime 'Inner', ya que fue modificada por inner_function

outer_function()
