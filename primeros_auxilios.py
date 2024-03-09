respuesta = input("¿Responde a Estímulos? [Si/No] : \n")
if respuesta.lower() == "si":
    print("Valorar la necesidad de llevar al hospital más cercano.")
else:
    print("Abrir la vía Aérea.")
    respira = input("¿Respira? [Si/No] : \n")
    if respira.lower() == "si":
        print("Permitirle posición de suficiente ventilación.")
    else:
        print("Administrar 5 Ventilaciones y llamar a la Ambulancia.")
        signos_vida = input("¿Signos de Vida? [Si/No] : \n")
        if signos_vida.lower() == "si":
            print("Reevaluar a la espera de la Ambulancia.")
        else:
            print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
        ambulancia = input("¿Llegó la ambulancia? [Si/No] : \n")
        while ambulancia != "si":
            signos_vida = input("¿Signos de Vida? [Si/No] : \n")
            if signos_vida.lower() == "si":
                print("Reevaluar a la espera de la Ambulancia.")
                ambulancia = input("¿Llegó la ambulancia? [Si/No] : \n")
            else:
                print("Administrar compresiones torácicas hasta que llegue la ambulancia.")
                ambulancia = input("¿Llegó la ambulancia? [Si/No] : \n")
        print ("Paciente rumbo al Hospital.")
