operador_valido = False
#Ingreso de operador del sistema
while not operador_valido:
    operador = input("Ingrese operador: ")
    if operador.isalpha():
        operador_valido = True
    else:
        print("Solo puede ingresar letras")

salida = False #Controlador del bucle
#Agenda
lunes_1 = ""
lunes_2 = ""
lunes_3 = ""
lunes_4 = ""
martes_1 = ""
martes_2 = ""
martes_3 = ""

#Ingreso al menú
while not salida:
    print("\n1 - Reservar turno")
    print("2 - Cancelar turno")
    print("3 - Ver agenda del día")
    print("4 - Ver resumen general")
    print("5 - Cerrar sistema")
    opcion = input("Elija una opción: ")
    if opcion.isdigit():
        match opcion:
            case "1": #Reservar el turno
                print("\nSeleccione el día:\n1 - Lunes\n2 - Martes")
                dia = input("Día: ") #Seleccionar el día solo en números
                if dia.isdigit():
                    match dia:
                        case "1":
                            paciente = input("Nombre del paciente: ")
                            if paciente.isalpha():
                                paciente = paciente.lower() #Para mayor coincidencia pasamos a minuscula todo
                                #Comprobación de coincidencia en turnos
                                if paciente == lunes_1 or paciente == lunes_2 or paciente == lunes_3 or paciente == lunes_4:
                                    print("Error: el paciente ya posee turno para ese día.")
                                #Asignación del primer turno disponible
                                if lunes_1 == "":
                                    lunes_1 = paciente
                                    print("Lunes 1: Turno asignado exitosamente")
                                elif lunes_2 == "":
                                    lunes_2 = paciente
                                    print("Lunes 2: Turno asignado exitosamente")
                                elif lunes_3 == "":
                                    lunes_3 = paciente
                                    print("Lunes 3: Turno asignado exitosamente")
                                elif lunes_4 == "":
                                    lunes_4 = paciente
                                    print("Lunes 4: Turno asignado exitosamente")
                                else:
                                    print("No quedan turnos disponibles para el día seleccionado")
                        case "2":
                            paciente = input("Nombre del paciente: ")
                            if paciente.isalpha():
                                paciente = paciente.lower()
                                #Comprobación de paciente con turno
                                if paciente == martes_1 or paciente == martes_2 or paciente == martes_3:
                                    print("Error: el paciente ya posee turno para ese día.")
                                #Asignación del primer turno disponible
                                if martes_1 == "":
                                    martes_1 = paciente
                                    print("Martes 1: Turno asignado exitosamente")
                                elif martes_2 == "":
                                    martes_2 = paciente
                                    print("Martes 2: Turno asignado exitosamente")
                                elif martes_3 == "":
                                    martes_3 = paciente
                                    print("Martes 3: Turno asignado exitosamente")
                                else:
                                    print("No quedan turnos disponibles para el día seleccionado")
                        case _:
                            print("Error: opción inválida")
                else:
                    print("Error: ingrese un número válido")
            case "2": #Cancelar un turno
                print("Seleccione el día:\n1 - Lunes\n2 - Martes")
                dia = input("Día: ")
                if dia.isdigit():
                    match dia:
                        case "1":
                            paciente = input("Nombre del paciente: ")
                            if paciente.isalpha():
                                paciente = paciente.lower()
                                #Búsqueda del paciente turno por turno del día Lunes
                                if paciente == lunes_1:
                                    lunes_1 = ""
                                    print("El turno ha sido cancelado")
                                elif paciente == lunes_2:
                                    lunes_2 = ""
                                    print("El turno ha sido cancelado")
                                elif paciente == lunes_3:
                                    lunes_3 = ""
                                    print("El turno ha sido cancelado")
                                elif paciente == lunes_4:
                                    lunes_4 = ""
                                    print("El turno ha sido cancelado")
                                else:
                                    print("El paciente no posee turno en el día seleccionado")
                        case "2":
                            paciente = input("Nombre del paciente: ")
                            if paciente.isalpha():
                                paciente = paciente.lower()
                                #Búsqueda del paciente turno por turno del día Martes
                                if paciente == martes_1:
                                    martes_1 = ""
                                    print("El turno ha sido cancelado")
                                elif paciente == martes_2:
                                    martes_2 = ""
                                    print("El turno ha sido cancelado")
                                elif paciente == martes_3:
                                    martes_3 = ""
                                    print("El turno ha sido cancelado")
                                else:
                                    print("El paciente no posee turno en el día seleccionado")
                        case _:
                            print("Error: opción inválida.")
            case "3":
                #Comprobación de agenda por día
                print("Seleccione el día:\n1 - Lunes\n2 - Martes")
                dia = input("Día: ")
                if dia.isdigit():
                    match dia:
                        case "1":
                            print("\nTurnos del día Lunes:")
                            if lunes_1 == "":
                                print("Lunes_1: Libre")
                            else:
                                print(f"Lunes 1: {lunes_1}")
                            if lunes_2 == "":
                                print("Lunes 2: Libre")
                            else:
                                print(f"Lunes 2: {lunes_2}")
                            if lunes_3 == "":
                                print("Lunes 3: Libre")
                            else:
                                print(f"Lunes 3: {lunes_3}")
                            if lunes_4 == "":
                                print("Lunes 4: Libre")
                            else:
                                print(f"Lunes 4: {lunes_4}")
                        case "2":
                            print("\nTurnos del día Martes:")
                            if martes_1 == "":
                                print("Martes 1: Libre")
                            else:
                                print(f"Martes 1: {martes_1}")
                            if martes_2 == "":
                                print("Martes 2: Libre")
                            else:
                                print(f"Martes 2: {martes_2}")
                            if martes_3 == "":
                                print("Martes 3: Libre")
                            else:
                                print(f"Martes 3: {martes_3}")
            case "4":
                #Acumuladores para turnos libres y disponibles
                lunes_ocupados = 0
                lunes_libres = 0
                martes_ocupados = 0
                martes_libres = 0
                #Suma de turnos libres u ocupados
                if lunes_1 == "":
                    lunes_libres += 1
                else:
                    lunes_ocupados += 1
                if lunes_2 == "":
                    lunes_libres += 1
                else:
                    lunes_ocupados += 1
                if lunes_3 == "":
                    lunes_libres += 1
                else:
                    lunes_ocupados += 1
                if lunes_4 == "":
                    lunes_libres += 1
                else:
                    lunes_ocupados += 1
                if martes_1 == "":
                    martes_libres += 1
                else:
                    martes_ocupados += 1
                if martes_2 == "":
                    martes_libres += 1
                else:
                    martes_ocupados += 1
                if martes_3 == "":
                    martes_libres += 1
                else:
                    martes_ocupados += 1
                #Salida en pantalla
                print("\nLunes")
                print(f"Tenes {lunes_libres} turnos disponibles y {lunes_ocupados} ocupados")
                print("Martes")
                print(f"Tenes {martes_libres} turnos disponibles y {martes_ocupados} ocupados")
                #Comprobación de días con más turnos
                if lunes_ocupados > martes_ocupados:
                    print("El Lunes es el día con más turnos ocupados")
                elif martes_ocupados > lunes_ocupados:
                    print("El Martes es el día con más turnos ocupados")
                else:
                    print("Tenés la misma cantidad de turnos ocupados en ambos días")
            case "5": #Salida del sistema
                salida = True
            case _:#En caso de ingresar cualquier otro número
                print("Error: opción inválida")
    else:
        print("Error: ingrese un número válido")