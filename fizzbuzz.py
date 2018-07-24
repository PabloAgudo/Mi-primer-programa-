

numeros = [1,2,5,15,6,3,5,20,30,60,70, 40, 33]

for indice in range(len(numeros)):

    n_ind = numeros[indice]
    valor = ""
    if n_ind % 3 == 0:
        valor += "Fizz"
    if n_ind % 5 == 0:
        valor += "Buzz"
    if n_ind % 3== 0  and n_ind %5== 0:
        valor = "BAZINGA"
    if valor != "":
        numeros[indice] = valor

print(numeros)



