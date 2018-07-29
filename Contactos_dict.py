agenda = dict()

restuesta = ""

while not restuesta == "Salir":
    print("--------------------------------------------")
    restuesta = input("Que quieres hacer: (Salir / Consultar Amigo [C] / Guardar Amigo [G]): ")


    #Guardar numero
    if restuesta == "G":
        print("Vamos a guardar Amigo")
        nonbre_añadir = input("Cual es el nombre??: ")
        numero_telf = input("Cual es el dia de nacimiento??: ")

        agenda[nonbre_añadir] = numero_telf

        print("Numero guardado con exito.")

    #Consultar numero
    elif restuesta == "C":
        nonbre_buscar = input("Quien quieres buscar: ")
        print("Su dia de nacimiento es: {} ".format(agenda[nonbre_buscar]))

