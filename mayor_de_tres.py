oportunidades = 5
number_to_guess = 2

user_number = int(input("Adibina un numero: "))

if number_to_guess == user_number:
    print("Has ganado")
else:
    print("intentalo de nuevo")
    oportunidades = oportunidades -1
    print("Oportunidades {}".format(oportunidades))

    if oportunidades == 0:
        print("has perdido")
    else:
        user_number = int(input("Adibina un numero: "))

        if number_to_guess == user_number:
            print("Has ganado")
        else:
            print("intentalo de nuevo")
            oportunidades = oportunidades - 1
            print("Oportunidades {}".format(oportunidades))

            if oportunidades == 0:
                print("has perdido")
            else:
                user_number = int(input("Adibina un numero: "))

                if number_to_guess == user_number:
                    print("Has ganado")
                else:
                    print("intentalo de nuevo")
                    oportunidades = oportunidades - 1
                    print("Oportunidades {}".format(oportunidades))

                    if oportunidades == 0:
                        print("has perdido")
                    else:
                        user_number = int(input("Adibina un numero: "))

                        if number_to_guess == user_number:
                            print("Has ganado")
                        else:
                            print("intentalo de nuevo")
                            oportunidades = oportunidades - 1
                            print("Oportunidades {}".format(oportunidades))

                            if oportunidades == 0:
                                print("has perdido")
                            else:
                                user_number = int(input("Adibina un numero: "))

                                if number_to_guess == user_number:
                                    print("Has ganado")
                                else:
                                    print("intentalo de nuevo")
                                    oportunidades = oportunidades - 1
                                    print("Oportunidades {}".format(oportunidades))

                                    if oportunidades == 0:
                                        print("Has Perdido")





