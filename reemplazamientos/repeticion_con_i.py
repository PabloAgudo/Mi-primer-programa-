
n_vocales = 1
frase = input("Digame una frase: ")

for letra in frase:
    if letra == "a":
        frase = frase.replace("a", str(n_vocales), 1)
        n_vocales += 1
    elif letra == "e":
        frase = frase.replace("e", str(n_vocales), 1)
        n_vocales += 1
    elif letra == "i":
        frase = frase.replace("i", str(n_vocales), 1)
        n_vocales += 1
    elif letra == "o":
        frase = frase.replace("o", str(n_vocales), 1 )
        n_vocales += 1
    elif letra == "u":
        frase = frase.replace("u", str(n_vocales), 1)
        n_vocales += 1
print(frase)

