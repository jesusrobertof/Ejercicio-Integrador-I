idProducto = [1, 2, 3]
producto = ["Maíz grano", "Pepino", "Tomate verde"]
costoPorCaja = [285.55, 334.72, 129.00]
venta_productos = [
[2, 122],
[1, 89],
[1, 22],
[3, 48],
[1, 75],
[3, 322],
[2, 95],
[1, 148],
[1, 83],
[3, 100]
]# [ID_producto, cajas_vendidas]

numeroCajas = int(input ("Número de cajas a vender: "))
elegirProducto = int(input ("ID del producto: "))

venta_productos.append([elegirProducto, numeroCajas])
totalCajas = 0
for cajas in venta_productos:
    totalCajas += cajas[-1]

if (numeroCajas <= 100):
    costoEnvio = 1500
else:
    costoEnvio = 0
descuento = totalCajas>=1500

if (elegirProducto == 1):
    print ("El producto es: " + producto[0])
    print ("El precio por caja es: " + str(costoPorCaja[0]))
    pagoTotal = (costoPorCaja[0]*numeroCajas) + costoEnvio
    if (descuento == True):
        pagoTotal = pagoTotal - (pagoTotal*0.20)
    print ("Aplica descuento del 20%: ", descuento)
    print ("El costo total a pagar: ", pagoTotal)
elif (elegirProducto == 2):
    print ("El producto es: " + producto[1])
    print ("El precio por caja es: " + str(costoPorCaja[1]))
    pagoTotal = (costoPorCaja[1]*numeroCajas) + costoEnvio
    if (descuento == True):
        pagoTotal = pagoTotal - (pagoTotal*0.20)
    print ("Aplica descuento del 20%: ", descuento)
    print ("El costo total a pagar: ", pagoTotal)
elif (elegirProducto == 3):
    print ("El producto es: " + producto[2])
    print ("El precio por caja es: " + str(costoPorCaja[2]))
    pagoTotal = (costoPorCaja[2]*numeroCajas) + costoEnvio
    if (descuento == True):
        pagoTotal = pagoTotal - (pagoTotal*0.20)
    print ("Aplica descuento del 20%: ", descuento)
    print ("El costo total a pagar: ", pagoTotal)
else: 
    print("ID de producto no válido")