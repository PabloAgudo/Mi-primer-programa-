signos = [".", ",", "!", "¡", "?", "¿", ":", ";"]
aparicion_palabras = dict()

texto = input("Introduzca un texto: ")
indice = 0
texto += " "
palabras_texto = []
caracteres = ["", ]


for letra in texto:
    if letra == " ":
        palabras_texto.append(caracteres[0])
        caracteres = [""]
    elif letra in signos:
        palabras_texto.append(caracteres[0])
        caracteres = [""]
    else:
        caracteres[0] += letra


for palabra in palabras_texto:
    if palabra in aparicion_palabras:
        aparicion_palabras[palabra] +=1
    else:
        aparicion_palabras[palabra] = 1

for cantidad_de_palabras in aparicion_palabras:
    print("{}: {}".format(cantidad_de_palabras, aparicion_palabras[cantidad_de_palabras]))
    print("")
