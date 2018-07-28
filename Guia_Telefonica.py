agenda = []

restuesta = ""

while not restuesta == "Salir":
    print("--------------------------------------------")
    restuesta = input("Que quieres hacer: (Salir / Consultar numero [C] / Guardar numero [G]): ")


    #Guardar numero
    if restuesta == "G":
        print("Vamos a guardar un numero de telefono")
        nonbre_añadir = input("Cual es el nombre??: ")
        numero_telf = input("Cual es el numero??: ")

        agenda.append([nonbre_añadir, numero_telf])

        print("Numero guardado con exito.")

    #Consultar numero
    elif restuesta == "C":
        nonbre_buscar = input("Quien quieres buscar: ")

        for nombre_numero in agenda:
            if nombre_numero[0] == nonbre_buscar:
                print("Su numero de telefono es: {} ".format(nombre_numero[1]))

