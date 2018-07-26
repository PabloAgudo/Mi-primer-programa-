
def reverse_string(str_to_reverse):
    str_to_reverse = input("Dime una str: ")
    posicion_letra = -1
    str_mod = ""
    for letra in str_to_reverse:
        str_mod += str_to_reverse[posicion_letra]
        posicion_letra += 1

    return str_mod


reverse_string()
print(str_to_reverse)



