numero_vocales = 0
numero_consonates = 0

frase = input("Introduce una frase:")

vocales = ["a", "e", "i", "o", "u"]

for letra in frase:
    encontrado = False
    for vocal in vocales:
        if  vocal == letra:
            numero_vocales += 1
            encontrado = True
        elif encontrado == False:
            if vocal == "u":
                if letra != " ":
                    numero_consonates += 1

print("El Numero de Vocales es: {}".format(numero_vocales))
print("El numero de Consonates es:{}".format(numero_consonates))
