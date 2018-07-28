numero_vocales = 0
numero_consonates = 0
n_espacios = 0
n_puntos = 0
n_comas = 0
n_mayusculas = 0
n_minusculas = 0
secuencia_vocales = []
mayuscula = ""
lista_simbolos = [" ", ".", ",", "?", "¿", "!", "¡", "-"]

frase = input("Introduce una frase:")

vocales = ["a", "e", "i", "o", "u"]

for letra in frase:
    if letra in vocales:
        numero_vocales += 1
        secuencia_vocales.append(letra)
        #Mayusculas
        mayuscula = str.capitalize(letra)
        if mayuscula == letra:
            n_mayusculas +=1
        else:
            n_minusculas +=1
    else:
        if letra in lista_simbolos:
            if letra == " ":
                n_espacios += 1
            elif letra == ".":
                n_puntos += 1
            elif letra == ",":
                n_comas += 1

        else:
            numero_consonates +=1
            # Mayusculas
            mayuscula = str.capitalize(letra)
            if mayuscula == letra:
                n_mayusculas += 1
            else:
                n_minusculas += 1

print("LETRAS")
print("El Numero de Vocales es: {}".format(numero_vocales))
print("El numero de Consonates es:{}".format(numero_consonates))
print("El numero de Mayusculas es:{}".format(n_mayusculas))
print("El numero de Minusculas es:{}".format(n_minusculas))

print("SIMBOLOS")
print("El numero de Espacios es:{}".format(n_espacios))
print("El numero de Puntos es:{}".format(n_puntos))
print("El numero de Comas es:{}".format(n_comas))

print("Por otra parte")
print("La secuenca de vocales es:")
print(secuencia_vocales)