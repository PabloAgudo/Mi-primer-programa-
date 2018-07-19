

vida_pika = 100
vida_bulbasur = 120
vida_charmander = 80
vida_squirtel = 100

daño_bulbasur = 7
daño_charmander = 12
daño_squirtel = 10


enemigo = input("Contra quien quieres pelear??  (Bulbasur/Charmander/Squirtel):").upper()
print(enemigo)

if enemigo == "BULBASUR":
    vida_enemiga = vida_bulbasur
    ataque_enemigo = daño_bulbasur
if enemigo == "CHARMANDER":
    vida_enemiga = vida_charmander
    ataque_enemigo = daño_charmander
if enemigo == "SQUIRTEL":
    vida_enemiga = vida_squirtel
    ataque_enemigo = daño_squirtel
else:
    print("Dato Incorrecto. Elegire un pokimon Aleatorio")
    vida_enemiga = vida_charmander
    ataque_enemigo = daño_charmander
    enemigo = "CHARMANDER"

print("Has Elegido a {}".format(enemigo))
print("Preparate para la batalla")



print(vida_enemiga)
print(ataque_enemigo)
