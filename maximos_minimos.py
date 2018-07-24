largo_lista  = 0
n_usuario = ""
numeros_usuario = []

while len(numeros_usuario) < 10:
    n_usuario = input("Dime un numero: ")
    if  n_usuario.isdigit():
        numeros_usuario.append(int(n_usuario))
        n_usuario = ""
        print("Numero añadido")
        largo_lista += 1
    else:
        print("Error")

#Comparacion

numero_grande = max(numeros_usuario)
print("El numero mas grande es: {}".format(numero_grande))

#Media

n_total = 0
for numero in numeros_usuario:
    n_total = numero + n_total
print("La media es: {} ".format(n_total/largo_lista))

