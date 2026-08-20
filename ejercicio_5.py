#Validación de ingreso de nombre del gladiador
print("=== BIENVENIDO A LA ARENA ===")
gladiador_valido = False #Controlador del ingreso de gladiador
while not gladiador_valido:
    gladiador = input("Nombre del gladiador: ")
    if gladiador.isalpha():
        gladiador_valido = True
    else:
        print("Error: Solo se permiten letras")
print(f"¡Bienvenido gladiador {gladiador}")
print("=== INICIO DEL COMBATE ===")
#Variables iniciales
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True
#Ciclo de combate
while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"{gladiador} (HP: {vida_gladiador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones_vida}")
    #Turno del gladiador
    while turno_gladiador:
        #No salir del menú hasta validar el ingreso de números correctos
        menu_valido = False
        while not menu_valido:
            print("\nOpciones:\n1 - Ataque rápido\n2 - Ráfaga veloz\n3 - Curar")
            opcion = input("Opción: ")
            if opcion.isdigit():
                #Conversión a entero para manejo de match/case
                opcion = int(opcion)
                if 1 <= opcion <=3:
                    match opcion:
                        case 1:
                            #Ataque rápido
                            #Si la vida del enemigo es menor a 20 puntos, el jugador realiza un "Golpe Crítico" multiplicando su daño base por 1.5
                            if vida_enemigo < 20:
                                golpe_critico = ataque_pesado * 1.5
                                vida_enemigo -= golpe_critico
                                print(f"¡Atacaste al enemigo por {golpe_critico} puntos de daño!")
                            #Si la vida del enemigo es mayor a 20 puntos, el jugador realiza un golpe normal
                            else:
                                vida_enemigo -= ataque_pesado
                                print(f"¡Atacaste al enemigo por {ataque_pesado} puntos de daño!")
                            turno_gladiador = False
                        case 2:
                            #Ráfaga veloz
                            print("!Inicias una ráfaga de golpes!")
                            #Esta acción realiza una serie de golpes rápidos.
                            for i in range(3):
                                vida_enemigo -= 5
                                print("¡Golpe conectado por 5 de daño!")
                            turno_gladiador = False
                        case 3:
                            #Curar si aún tiene pociones
                            if pociones_vida > 0:
                                pociones_vida -= 1
                                vida_gladiador += 30
                                print("¡Recuperaste 30 puntos de vida")
                            #Si no quedan pociones pierde el turno
                            else:
                                print("¡No te quedan pociones, pierdes el turno!")
                            turno_gladiador = False
                    menu_valido = True
                else:
                    print("Error: opción inválida")
            else:
                print("Error: sólo puedes ingresar números")
    #Turno del enemigo, sólo si aún tiene puntos de vida
    if not turno_gladiador and vida_enemigo > 0:
        vida_gladiador -= danio_enemigo
        print("¡El enemigo contraataca por 12 puntos!")
        print("=== NUEVO TURNO ===")
        turno_gladiador = True
#Cálculo y muestra de resultado final de la batalla
if vida_gladiador > 0:
    print(f"¡VICTORIA! {gladiador} ha ganado la batalla.")
elif vida_gladiador <= 0:
    print("¡DERROTA! Has caído en combate")