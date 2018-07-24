

apetece_helado_input = input("Te Apetece Un Helado?  (Si/No): ").upper()

if apetece_helado_input == "SI":
    apetece_helado = True
elif apetece_helado_input == "NO":
    apetece_helado = False
else:
    print("Dato incorrecto Te quedas sin heladi")
    apetece_helado = False


tienes_dinero_input = input("Tienes dinero para un helado (Si/No) ").upper()
esta_el_señor_de_los_helados_input = input("Esta el señor de los helados (Si/No) ").upper()
esta_tu_tia_input = input("Estas con tu tia? (Si/No)").upper()


puedes_comprarlo = tienes_dinero_input== "SI" or esta_tu_tia_input =="SI"
esta_el_señor_de_los_helados = esta_el_señor_de_los_helados_input=="SI"


if  apetece_helado and puedes_comprarlo and esta_el_señor_de_los_helados :
    print("Comete un helado")
else:
    print("Comete una verga")

