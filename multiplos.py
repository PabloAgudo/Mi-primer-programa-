multiplos_dos = []
multiplos_tres = []
multiplo_cinco = []
multiplo_siete = []

numeros_del_usuario = []

while len(numeros_del_usuario) < 10:
    numeros_del_usuario.append(int(input("Dime un numero: ")))


for indice in range(len(numeros_del_usuario)):
    n_ind = numeros_del_usuario[indice]
    if n_ind % 2 == 0:
        multiplos_dos.append(n_ind)
    if n_ind % 3 == 0:
        multiplos_tres.append(n_ind)
    if n_ind % 5 == 0:
        multiplo_cinco.append(n_ind)
    if n_ind % 7 == 0:
        multiplo_siete.append(n_ind)

print("Multiplos de dos: {}".format(multiplos_dos))
print("Multiplos de tres: {}".format(multiplos_tres))
print("Multiplos de cinco: {}".format(multiplo_cinco))
print("Multiplos de siete: {}".format(multiplo_siete))


