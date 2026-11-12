# uso input para meter un dato que se leerá y float para convertir ese dato en numeros
importe = float(input("Importe de la compra (€): "))
entregado = float(input("Dinero entregado (€): "))

# pasamos los datos a centimos multiplicando por 100, redondeamos el numero con round para q no haya decimales y ponemos el resultado en otra variable
# a lo largo de este codigo uso operaciones matematicas que creo q no hacen falta explicar como la multiplicacion con "*", la division con "/" y el "//" que divide y se queda solo con la parte entera sin los decimales
cambio = round(entregado * 100) - round(importe * 100)

# pasamos esto a euros dividiendo entre 100
print("Cambio:", cambio / 100, "€")

# para cada billete o moneda de 20 euros a 5 centimos, el "//" da cuantos caben en el cambio en centimos y el "%" deja lo q falta por devolver con los siguientes
billetes20 = cambio // 2000
cambio = cambio % 2000

# se repite lo mismo con los demás billetes y monedas
billetes10 = cambio // 1000
cambio = cambio % 1000

billetes5 = cambio // 500
cambio = cambio % 500

monedas2 = cambio // 200
cambio = cambio % 200

monedas1 = cambio // 100
cambio = cambio % 100

monedas50 = cambio // 50
cambio = cambio % 50

monedas20 = cambio // 20
cambio = cambio % 20

monedas10 = cambio // 10
cambio = cambio % 10

# esta parte solo tiene una linea en vez de una porque es la última moneda así q no hace falta calcular el resto con el "%" porque ya no quedan más monedas por repartir
monedas5 = cambio // 5

# esta parte nos da texto usando print sobre cuántos billetes y monedas de cada tipo hay q devolver usando las variables q calculamos antes
print("Billetes de 20 €:", billetes20)
print("Billetes de 10 €:", billetes10)
print("Billetes de 5 €:", billetes5)
print("Monedas de 2 €:", monedas2)
print("Monedas de 1 €:", monedas1)
print("Monedas de 50 cént.:", monedas50)
print("Monedas de 20 cént.:", monedas20)
print("Monedas de 10 cént.:", monedas10)
print("Monedas de 5 cént.:", monedas5)