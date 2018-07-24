

numeros = [1,2,5,9,6,3,5,20,30,60,70,]

for indice in range(len(numeros)):

    n_ind = numeros[indice]
    valor = ""
    if n_ind % 3 == 0:
        valor += "Fizz"
    if n_ind % 5 == 0:
        valor += "Buzz"
    if valor != "":
        numeros[indice] = valor
print(numeros)



