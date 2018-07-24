
n_usuario = ""
numeros_usuario = []

while len(numeros_usuario) < 10:
    n_usuario = input("Dime un numero: ")
    if  n_usuario.isdigit():
        numeros_usuario.append(int(n_usuario))
        n_usuario = ""
        print("Numero añadido")
    else:
        print("Error")

numero_grande = numeros_usuario [0]