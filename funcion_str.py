
def reverse_string(str_to_reverse):
    posicion_letra = -1
    str_mod = ""
    for letra in str_to_reverse:
        str_mod += str_to_reverse[posicion_letra]
        posicion_letra -= 1

    return str_mod


print(reverse_string("Hola"))
print(reverse_string("estenocleidomastoideo"))
print(reverse_string("olaf"))
print(reverse_string("paco el paquito me comio el pepenito"))





