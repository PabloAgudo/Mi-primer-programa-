

lista= [5, 6, "holas",88, 0.02, 5, 89, 0.003, "holololol", "aguacate"]
lista_str = []
lista_n = []
for dato in lista:
    if type(dato) == type("gsa"):
        lista_str.append(dato)
    else:
        lista_n.append(dato)
print(lista_str)
print(lista_n)