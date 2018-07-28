
rango = range(0,11)
numero = int(input("Dime un numero : "))

def numero_in_rango (numero, rango):
    confirmacion = False
    for nun in rango:
        if nun == numero:
            confirmacion = True

    return confirmacion
print(numero_in_rango(numero,rango ))