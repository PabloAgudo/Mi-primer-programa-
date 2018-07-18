oportunidades = 5
number_to_guess = 2
victoria = False

while oportunidades != 0:
    user_number = int(input("Adibina un numero: "))
    if number_to_guess == user_number:
        oportunidades = 0
        victoria = True
    else:
         print("intentalo de nuevo")
         oportunidades -= 1
         print("Oportunidades {}".format(oportunidades))

if victoria:
    print("Has Ganado")
else:
    print("Has Perdido")



