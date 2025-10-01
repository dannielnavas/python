variable_global = "Soy una variable global"
def local_function():
    variable_local = "Soy una variable local"
    print(variable_local)

local_function()
#print(variable_local)  # Esto generará un error porque variable_local no está definida en este ámbito global

def show_global():
    print(variable_global)

show_global()
