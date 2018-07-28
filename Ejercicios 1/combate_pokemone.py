

vida_pika = 100
vida_enemiga = 0
ataque_enemigo = 0

pokemon_elegido = (input("Contra quien quieres pelear??  (bulbasur/ charmander/ squirtel) : "))

if pokemon_elegido == "bulbasur":
    vida_enemiga = 120
    ataque_enemigo = 7
    pokemon_elegido = "Bulbasur"
    print("Has elejido a Bulbasur")

elif pokemon_elegido == "charmander":
    vida_enemiga = 80
    ataque_enemigo = 12
    pokemon_elegido = "Charmander"
    print("Has elejido a Charmander")

elif pokemon_elegido == "squirtel":
    vida_enemiga = 100
    ataque_enemigo = 10
    pokemon_elegido = "Squirtel"
    print("Has elejido a Squirtel")

else:
    print("Dato Incorrecto. Elijo yo Pokimon")
    vida_enemiga = 80
    ataque_enemigo = 12
    pokemon_elegido = "Charmander"
    print("Te a Tocado a Charmander")

print("Preparate para la batalla")


while vida_pika > 0 and vida_enemiga > 0 :

    print("Tu turno")
    ataque = input("Elije ataque (Rayito / Escupio): ")

    if ataque == "Rayito":
        vida_enemiga -= 10
        print("{} Sufre 10 de Daño".format(pokemon_elegido))
    else:
        if vida_enemiga < 20:
            vida_enemiga = 0
            print("CRITICO")
        else:
            vida_enemiga -=7
            print("{} Sufre 7 de Daño".format(pokemon_elegido))
    print("Vida enemiga:{}".format(vida_enemiga))

    if vida_enemiga > 0:
        print("Turno Enemigo")
        vida_pika -= ataque_enemigo
        print("Recives {} de Daño".format(ataque_enemigo))
        print("Tienes {} de Vida".format(vida_pika))




if vida_pika > 0:
    print("GANASTE")
if vida_enemiga > 0:
    print("PERDISTE")