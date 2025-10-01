x = 'Global'

def outer_function():
    x = 'Outer'

    def inner_function():
        x = 'Inner'
        print("Inner:", x)  # Imprime 'Inner'

    inner_function()
    print("Outer:", x)      # Imprime 'Outer'

outer_function()
print("Global:", x)        # Imprime 'Global'
