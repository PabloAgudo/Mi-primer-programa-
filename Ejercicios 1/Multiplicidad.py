


numero_usuario = int(input("Numero que quieres la tablad e multiplicar:"))

tabla = range(1,11)

for multiplo in tabla:

    if numero_usuario*multiplo/2 == int(numero_usuario*multiplo/2):
        print("{} * {} = {}".format(multiplo, numero_usuario, numero_usuario*multiplo) )
