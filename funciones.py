
def input_con_confirmacion (pregunta):
    confirmacion = False
    dato_usuario = ""


    while not confirmacion:
        dato_usuario = input(pregunta)
        seguro = input("Has dicho {}, ¿Estas seguro? (Si/No): ".format(dato_usuario))
        if seguro == "Si":
            confirmacion = True

    return dato_usuario





nonbre = input_con_confirmacion("Dime un numero: ")
print("Confirmamos el numero: {}".format(nonbre))

lsita = []
lsita.append