#Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

agente_valido = False #Controlador del ingreso de agente
while not agente_valido:
    agente = input("Nombre del agente: ")
    if agente.isalpha():
        agente_valido = True
    else:
        print("Solo puede ingresar letras")
print(f"¡Bienvenido agente {agente}")

bloqueo = False
forzar_cerradura = 0 #acumulador de intentos de forzar cerraduras
#El juego continúa mientras: energia > 0, tiempo > 0, cerraduras_abiertas < 3 y no esté bloqueado por alarma.
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not bloqueo:
    #Estado del agente en cada turno
    print(f"\nEnergia: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    if not alarma:
        print(f"Alarma: desactivada")
    else:
        print(f"Alarma: activada")
    #Menú de acciones con validación de ingreso
    menu_valido = False
    while not menu_valido:
        #Salida del menú
        print("\nMenú:\n1 - Forzar cerradura\n2 - Hackear panel\n3 - Descansar")
        accion = input("Elija una acción: ")
        #Tomar como válido solo números del 1 al 3 (opciones del menú)
        if accion.isdigit():
            accion = int(accion)
            if 3 >= accion >=1:
                match accion:
                    #Forzar cerradura
                    case 1:
                        #Muestra el costo de la acción
                        energia -= 20
                        print("Su energía bajó 20")
                        tiempo -= 2
                        print("El tiempo bajó 2")
                        forzar_cerradura += 1
                        print(f"Lleva {forzar_cerradura} intentos consecutivos, al 3er intento se activará la alarma")
                        if forzar_cerradura >= 3:
                            print("La cerradura se trabó")
                            alarma = True
                        else:
                            if energia < 40: #Con energía menor a 40 se activa alarma si elige el 3
                                print("Hay riesgo de alarma")
                                numero_valido = False
                                #Validación de ingreso de número
                                while not numero_valido:
                                    numero = input("Ingrese un número del 1 al 3: ")
                                    if numero.isdigit():
                                        numero = int(numero)
                                        if numero == 3:
                                            print("La alarma se activó")
                                            numero_valido = True
                                            alarma = True
                                        elif (numero == 1 or numero == 2):
                                            if not alarma:
                                                cerraduras_abiertas += 1
                                                print("Cerradura abierta")
                                            else:
                                                print("La alarma está activada, la cerradura no abrió")
                                            numero_valido = True
                                        else:
                                            print("Error: número inválido")
                                    else:
                                        print("Error: Debe ingresar un número del 1 al 3")
                            elif not alarma:
                                #Si la emergia es mayor a 40 y la alarma no está activa
                                cerraduras_abiertas += 1
                                print("Cerradura abierta")
                            else:
                                #Si la alarma está activa no abre ninguna cerradura
                                print("La alarma está activada, la cerradura no abrió")
                    #Hackear panel
                    case 2:
                        #Muestra el costo de la acción
                        energia -= 10
                        print("Su energía bajó 10")
                        tiempo -= 3
                        print("El tiempo bajó 3")
                        forzar_cerradura = 0
                        #Pasos para abrir cerradura mostrando progreso
                        for i in range(4):
                            codigo_parcial += "a"
                            print(f"Paso {i +1}")
                            print("Descifrando el código....")
                        #Si el largo del código parcial es mayor a 8 abre una cerradura y luego reinicia el código parcial
                        if len(codigo_parcial) >= 8:
                            if cerraduras_abiertas < 3:
                                cerraduras_abiertas += 1
                                print("Código descifrado")
                                print("Abrió una cerradura")
                                codigo_parcial = ""
                    case 3:
                        #Muestra el costo de la acción
                        energia += 15
                        print("Descansando...su energía subió 15")
                        tiempo -=1
                        print("El tiempo bajó 1")
                        forzar_cerradura = 0
                        if alarma is True:
                            #Si la alarma está activa se restan 10 de energía
                            energia -= 10
                            print("Alarma activa, tu energía baja 10")
                        #El máximo de energía es 100
                        if energia >= 100:
                            energia = 100
                menu_valido = True
            else:
                print("Error: opción no válida")
        else:
            print("Error: debe ingresar un número")
    #Si la alarma está activada y el tiempo es menor a 3 el juego se bloquea y el agente pierde
    if alarma is True and tiempo <= 3:
        bloqueo = True

print("\n===================================")
if cerraduras_abiertas == 3:
    print(f"¡Victoria del agente {agente}!")
elif bloqueo is True:
    print(f"¡Derrota! Lo siento agente {agente}")
elif tiempo <= 0:
    print(f"¡Derrota! Lo siento agente {agente} el tiempo de agotó")
elif energia <= 0:
    print(f"¡Derrota! Lo siento agente {agente} se ha quedado sin energía")
print("===================================")