
aparicion_palabras = dict ()

texto = input("Introduzca un texto: ")


for palabra in texto:
    if palabra in aparicion_palabras:
        aparicion_palabras[palabra] +=1
    else:
        aparicion_palabras[palabra] = 1

print(aparicion_palabras)
