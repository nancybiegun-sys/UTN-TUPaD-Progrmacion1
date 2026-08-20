#interruptor del bucle while
cliente_valido = False

while not cliente_valido:
    #ingreso de usuario, borrando espacios vacios al principio y final de la palabra
    cliente = input("Por favor, ingrese solo el nombre del cliente: ").strip()
    if cliente.isalpha():
        print(f"Cliente: {cliente}")#ingreso valido
        cliente_valido = True
    else:
        print("Error: Ingrese solo letras")

#Validación de la cantidad de productos
cantidad_valida = False

while not cantidad_valida:
    cant_productos = input("Ingrese la cantidad de productos a comprar: ")
    if cant_productos.isdigit():#Verificar si son digitos
        cant_productos = int(cant_productos) #Transformar a enteros para poder verificar que sea mayor a 0
        if cant_productos > 0:
            print(f"Cantidad de productos: {cant_productos}")
            cantidad_valida = True
        else:
            print("Error: Debe ingresar números positivos")
    else:
        print("Error: Debe ingresar solo números enteros positivos")

#Acumuladores de precio total
total_sin_descuentos = 0
total_con_descuentos = 0

#Pedido de precios y descuentos por productos
for i in range(cant_productos):
    #Validación de precio como número entero positivo
    precio_valido = False
    while not precio_valido:
        precio = input(f"Por favor, ingrese el precio {i + 1}: ").strip()
        if precio.isdigit():
            precio = int(precio)
            if precio > 0:
                total_sin_descuentos += precio #Suma del precio al acumulador de total sin descuentos
                precio_valido = True
            else:
                print("Error: Debe ingresar números positivos")
        else:
            print("Error: Debe ingresar solo números enteros positivos")
    #Validación de descuento
    descuento_valido = False
    while not descuento_valido:
        descuento = input(f"¿El producto {i + 1} tiene descuento? (S/N): ").lower().strip()
        #De ambas maneras deben sumarse al total con descuentos
        if descuento == "s":
            total_con_descuentos += (precio * 0.9)
            descuento_valido = True
        elif descuento == "n":
            total_con_descuentos += precio
            descuento_valido = True
        else:
            print("Error: Ingrese S para si o N para no")
    print(f"Producto {i + 1} - Precio: {precio} Descuento (S/N): {descuento}")

#Calculo del promedio por producto
promedio_producto = (total_con_descuentos / cant_productos)
#Impresión de pantalla de los totales y promedio
print("=================================================")#Espacio para separar
print("=================================================")
print(f"Total sin descuento: ${total_sin_descuentos}")
print(f"Total con descuento: ${total_con_descuentos}")
print(f"Ahorro: ${total_sin_descuentos - total_con_descuentos}")
print(f"Promedio por producto: ${promedio_producto:.2f}")