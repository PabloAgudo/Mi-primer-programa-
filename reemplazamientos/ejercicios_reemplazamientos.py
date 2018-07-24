
str_a_cambiar = "Hola numero {}, numero {}, {} y {}"
valores_sustituir = [1, 2,"hola", "adios"]
for dato in valores_sustituir:
    str_a_cambiar = str_a_cambiar.replace("{}", str(dato), 1)

print(str_a_cambiar)