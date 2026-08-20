usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
intentos_maximos = 3
ingreso_valido = False
while not ingreso_valido and intentos < intentos_maximos:
    print(f"Intento {intentos + 1}/{intentos_maximos}")
    usuario_ingresado = input("Usuario: ")
    clave_ingresada = input("Clave: ")
    if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
        print("Acceso concedido.")
        ingreso_valido = True
    else:
        intentos += 1
        if intentos < intentos_maximos:
            print("Error: credenciales inválidas.")
#Bloqueo de la cuenta solo en caso de agotar intentos y no haber logrado el ingreso
if not ingreso_valido:
    print("Cuenta bloqueada.")
#Ingreso al sistema en caso de acceso concedido
else:
    salida = False
    while not salida:
        #Salida del menú de opciones
        print("\nElija una opción para continuar")
        print("1 - Ver estado de inscripción")
        print("2 - Cambiar clave")
        print("3 - Mostrar mensaje motivacional")
        print("4 - Salir")
        opcion_ingresada = input("Opción: ").strip()
        #Validación de número ingresado e ingreso a sus opciones
        if opcion_ingresada.isdigit():
            #Transformar en entero para la validación en match case
            opcion_ingresada = int(opcion_ingresada)
            match opcion_ingresada:
                case 1:
                    print("\nInscripto")
                case 2:
                    #Validación de cambio de clave, solo un intento y vuelve al menú
                    clave_1 = input("\nNueva clave (Al menos 6 caracteres): ")
                    #Validación de caracteres
                    if len(clave_1) >= 6:
                        clave_2 = input("Confirme la nueva clave: ")
                        #Confirmar que ambas claves coinciden y de ser así modificar la clave correcta
                        if clave_1 == clave_2:
                            clave_correcta = clave_1
                            print("\nContraseña cambiada con éxito")
                        else:
                            print("\nError: ambas claves deben coincidir")
                    else:
                        print("\nError: mínimo 6 caracteres")
                case 3:
                    print("\n¡Vas por buen camino, sigue así!")
                case 4:
                    #Finalizar el programa
                    print("\n¡Hasta la próxima!")
                    salida = True
                case _:
                    #En caso de ingresar cualquier otro número
                    print("\nError, opción fuera de rango")
        else:
            #En caso de ingresar otro caracter no numérico
            print("\nError, ingrese un número válido")