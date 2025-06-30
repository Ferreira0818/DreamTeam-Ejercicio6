import Funciones

equipo = {}


while True:
    print("Dream team")
    print("1)Registrar jugador")
    print("2)Buscar jugador por rut")
    print("3)Mostrar estado nutricional")
    print("4)Listar equipo completo")
    print("5)Contar jugadores por posicion")
    print("6)Salir")
    try:
        menu_op = int(input("Ingrese el numero de la opcion que desea: "))
        if menu_op <1 or menu_op >6:
            raise ValueError
    except ValueError:
        print("No ingrese caracteres o valores menores que 1 o mayores que 6")
    else:
        if menu_op == 1: #Registrar jugadores
            Funciones.registrar_jugadores(equipo)
        elif menu_op == 2: #Buscar jugadores
            if len(equipo)<1:
                print("No hay jugadores registrados. Intente agregar jugadores e intente nuevamente")
            else:
                print(Funciones.buscar_jugadores(equipo))
        elif menu_op == 3: #Mostrar estado nutricional
            if len(equipo)<1:
                print("No hay jugadores registrados. Intente agregar jugadores e intente nuevamente")
            else:
                print(Funciones.estado_nutricional(equipo))
        elif menu_op == 4: #Listar equipo completo
            if len(equipo)<1:
                print("No hay jugadores registrados. Intente agregar jugadores e intente nuevamente")
            else:
                print(Funciones.mostrar_equipo(equipo))
        elif menu_op == 5: #Contar jugadores por posición
            if len(equipo)<1:
                print("No hay jugadores registrados. Intente agregar jugadores e intente nuevamente")
            else:
                Funciones.contar_jugadores(equipo)
        elif menu_op == 6: #Salir
            print("Hasta luego.")
            break

    