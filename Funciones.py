equipo = {}



def registrar_jugadores(equipo):
    while True:
        try:
            rut = input("Ingrese el rut del jugador: ")
        except Exception as error:
            print(f"Error tipo: {error}")
        else:
            while True:
                try:
                    nombre = input("Ingrese el nombre del jugador: ")
                    if nombre.isdigit():
                        raise TypeError
                except TypeError:
                    print("El nombre no puede contener números")
                else:
                    while True:
                        try:
                            peso = float(input("Ingrese el peso del jugador en kilogramos: "))
                            if peso <1:
                                raise ValueError
                        except ValueError:
                            print("Ingrese solamente numeros y con valor positivo")
                        else:
                            while True:
                                try:
                                    estatura = float(input("Ingrese la estatura del jugador en metros: "))
                                    if estatura <1:
                                        raise ValueError
                                except ValueError:
                                    print("Ingrese solamente numeros y con valor positivos")
                                else:
                                    while True:
                                        try:
                                            print("Posiciones")
                                            print("1)Arquero")
                                            print("2)Defensa")
                                            print("3)Mediocampista")
                                            print("4)Delantero")
                                            posicion = int(input("Ingrese la opcion correspondiente a la posicion del jugador: "))
                                            if posicion <1 or posicion >4:
                                                raise ValueError
                                        except ValueError:
                                            print("Ingrese solamente el numero de la opcion que corresponde a la posicion del jugador")
                                        else:
                                            if posicion == 1:
                                                equipo[rut] = {"Nombre": nombre,"Peso": peso,"Estatura": estatura,"Posicion": "Arquero"} 
                                                break
                                            elif posicion == 2:
                                                equipo[rut] = {"Nombre": nombre,"Peso": peso,"Estatura": estatura,"Posicion": "Defensa"}
                                                break
                                            elif posicion == 3:
                                                equipo[rut] = {"Nombre": nombre,"Peso": peso,"Estatura": estatura,"Posicion": "Mediocampista"}
                                                break
                                            else:
                                                equipo[rut] = {"Nombre": nombre,"Peso": peso,"Estatura": estatura,"Posicion": "Delantero"}
                                                break
                                    break
                            break
                    break
            break

def buscar_jugadores(equipo):
    rut = input("Ingrese el rut del jugador")
    if rut in equipo:
        return(equipo[rut])
    else:
        return("Jugador no se encuentra registrado")
    
def estado_nutricional(equipo):
    rut = input("Ingrese el rut del jugador")
    if rut in equipo:
        jugador = equipo[rut];
        peso = jugador["Peso"]
        estatura = jugador["Estatura"]
        imc = peso/(estatura)*2
        return(f"El imc del jugador {rut} es {imc:f}")
    else:
        return(f"No hay jugadore con el {rut} registrado")

def mostrar_equipo(equipo):
    for jugador in equipo.values():
        return(f"Nombre: {jugador["Nombre"]} posicion: {jugador["Posicion"]}")

       
    
def contar_jugadores(equipo):
    arquero = 0
    defensa = 0
    mediocampo = 0
    delantero = 0
    
    for jugador in equipo.values():
        
        if jugador["Posicion"] == "Arquero":
            arquero +=1
        elif jugador["Posicion"] == "Defensa":
            defensa +=1
        elif jugador["Posicion"] == "Mediocampista":
            mediocampo +=1
        else:
            delantero +=1
    print("Actualmente, el equipo contiene: ")
    if arquero != 0:
        print(F"{arquero} arqueros")
    else:
        print("No hay arqueros registrados")
    if defensa != 0:
        print(f"{defensa} defensas")
    else:
        print("No hay defensas registrados")
    if mediocampo != 0:
        print(f"{mediocampo} mediocampistas")
    else:
        print("No hay mediocampistas registrados")
    if delantero !=0:
        print(F"{delantero} delanteros")
    else:
        print("No hay delanteros registrados")    