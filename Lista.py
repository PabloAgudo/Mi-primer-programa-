
mi_lista = []
input_usuario= ""
indice = 0

while input_usuario != "FIN":
     mi_lista.append(input_usuario)
     input_usuario = input("Que quieres comprar? : (Escribe FIN para terminar)")


for item in mi_lista:
    print("Compra {}".format(item))

print("Esta es tu lista")