from typing import Counter
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches

Saludo = """ 

Bienvenida a Life Store

Por favor, ingresa tu ID de identificación así como tu contraseña para acceder a la información relacionada a ventas, stock, etc. 

"""

print (Saludo)

# Con este primer código, el usuario puede acceder al ingreso de sesión.

if __name__ == "__main__":
    
    USUARIO = "Manager" 
    CONTRASEÑA = "LIFESTORE"

    username = input('Coloca tu nombre de usuario:\n > ')
    password = input('Ingresa tu contraseña:\n > ')

    if username == USUARIO:
        print("¡Bienvenida/o, Manager!")
        if password == CONTRASEÑA:
                print("Ingrese contraseña")
        else:
                print("Contraseña incorrecta")
    else: 
        print("El usuario no es correcto, verifique")

#Primer consigna: Productos más vendidos y productos rezagados
# Primer punto de la consigna: Este código es para calcular el TOP 5 de los productos más vendidos, así como el TOP 10 con mayores búsquedas

Consigna1_parte1 = """ 

CONSIGNA #1
A continuación verás un desplegado general del # de ventas anuales por ID de producto
"""
print ( Consigna1_parte1)

#Con este código creé una lista vacia en donde pudiera hacer match entré el ID del producto como con la cantidad de veces que se vendió. 
#En vez de contar la longitud de los productos, agregué el rango +1 para que saliera de manera directa. Investigué la función "diccionario" y con eso pude lograrlo.

import operator
producto_ventas=[]

for l in lifestore_sales:
    producto_ventas.append(l[1])

n_producto_ventas={}
for p in range(1,97):
    n_producto_ventas[p]=producto_ventas.count(p)

print(n_producto_ventas)

#Una vez ya investigada la función "diccionario" encontré una forma directa de sacar el TOP 5 a través de la definición de un operador.
#Sé que aún no vemos como tal esa función en el curso, sin embargo me ayudo a sacar de manera más sencilla la información. 

Consigna1_parte1_1 = """

A continuación verás el TOP 5 de los productos más vendidos en todo el año en LIFESTORE

"""
print(Consigna1_parte1_1)

n_producto_ventas_sort=sorted(n_producto_ventas.items(), key=operator.itemgetter(1), reverse=True)

top_5=[]
for n in range(0,5):
    top_5.append(n_producto_ventas_sort[n])

print(top_5)


# No había entendido que teníamos que hacer el Top 5 de manera mensual. Intenté hacer la relación diccionario entre fecha de venta y ID de producto, sin embargo no pude :( por lo que decidí sacar listas mensuales de venta y determinar el mayor - menor por mi cuenta.

Consigna_ventas_enero = """

A continuación el desplegado total de todas las ventas en ENERO 

"""

print(Consigna_ventas_enero)

meses = ['/01/','/02/','/03/','/04/','/05/','/06/','/07/','/08/','/09/','/10/','/11/','/12/']

Ventas_enero = []

for venta in lifestore_sales:
    fecha_venta_enero = venta [3]
    if meses [0] in fecha_venta_enero:
       Ventas_enero.append(venta)
print(Ventas_enero)

print("El total de ventas en el mes fue: ", len(Ventas_enero))

#Intenté sacar solamente los datos de meses con ID de producto, sin embargo al correr el código, me salió toda la info, la cual aunque no era exactamente los dos datos que quería, me dio la info que necesitaba para sacar Top ventas por mes"
#Fueron 12 listas, en total una por cada mes. 

print( """
IDs vendidos en el mes
""")

ids_enero = []

for venta in Ventas_enero:
    id=venta[1]
    ids_enero.append(id)
print(ids_enero)


Top5max_ventas_enero = """

Los 5 productos más vendidos en enero
"""
print(Top5max_ventas_enero)

Top_5_productos_mayores_ventas_ene = {"Más vendido": lifestore_products [2][1] , "2º más vendido" : lifestore_products [53][1] , "3º más vendido":lifestore_products [56][1], "4º más vendido": lifestore_products [3][1], "5º más vendido": lifestore_products [28][1]}
print(Top_5_productos_mayores_ventas_ene)


Top5min_ventas_enero = """

Los 5 productos menos vendidos en enero por categoría
"""
print(Top5min_ventas_enero)

Top_5_productos_menores_ventas_ene = {"Menos vendido": lifestore_products [88][1] , "2º menos vendido" : lifestore_products [50][1] , "3º menos vendido":lifestore_products [51][1], "4º menos vendido": lifestore_products [30][1], "5º menos vendido": lifestore_products [41][1]}
print(Top_5_productos_menores_ventas_ene)

Consigna_ventas_feb = """

A continuación el desplegado total de todas las ventas en FEBRERO 

"""

print(Consigna_ventas_feb)

Ventas_febrero = []

for venta in lifestore_sales:
    fecha_venta_febrero = venta [3]
    if meses [1] in fecha_venta_febrero:
       Ventas_febrero.append(venta)
print(Ventas_febrero)

print("El total de ventas en el mes fue: ", len(Ventas_febrero))

print( """
IDs vendidos en el mes
""")

ids_febrero = []

for venta in Ventas_febrero:
    id=venta[1]
    ids_febrero.append(id)
print(ids_febrero)


Top5max_ventas_febrero = """

Los 5 productos más vendidos en febrero
"""

print(Top5max_ventas_febrero)

Top_5_productos_mayores_ventas_feb = {"Más vendido": lifestore_products[53][1] , "2º más vendido" : lifestore_products[56][1] , "3º más vendido":lifestore_products[2][1], "4º más vendido": lifestore_products[4][1], "5º más vendido": lifestore_products[17][1]}
print(Top_5_productos_mayores_ventas_feb)


Top5min_ventas_febrero = """

Los 5 productos menos vendidos en febrero
"""
print(Top5min_ventas_febrero)

Top_5_productos_menores_ventas_feb = {"Menos vendido": lifestore_products[3][1] , "2º menos vendido" : lifestore_products[5][1] , "3º menos vendido":lifestore_products[6][1], "4º menos vendido": lifestore_products[7][1], "5º menos vendido": lifestore_products[11][1]}
print(Top_5_productos_menores_ventas_feb)


#
Consigna_ventas_mar = """

A continuación el desplegado total de todas las ventas en MARZO 

"""

print(Consigna_ventas_mar)

Ventas_marzo = []

for venta in lifestore_sales:
    fecha_venta_marzo = venta [3]
    if meses [2] in fecha_venta_marzo:
       Ventas_marzo.append(venta)
print(Ventas_marzo)

print("El total de ventas en el mes fue: ", len(Ventas_marzo))

print( """
IDs vendidos en el mes
""")

ids_marzo = []

for venta in Ventas_marzo:
    id=venta[1]
    ids_marzo.append(id)
print(ids_marzo)


Top5max_ventas_marzo = """

Los 5 productos más vendidos en marzo
"""

print(Top5max_ventas_marzo)

Top_5_productos_mayores_ventas_mar = {"Más vendido": lifestore_products [53][1] , "2º más vendido" : lifestore_products [2][1] , "3º más vendido":lifestore_products [11][1], "4º más vendido": lifestore_products [41][1], "5º más vendido": lifestore_products [41][1]}
print(Top_5_productos_mayores_ventas_mar)


Top5min_ventas_marzo = """

Los 5 productos menos vendidos en marzo
"""
print(Top5min_ventas_marzo)

Top_5_productos_menores_ventas_marzo = {"Menos vendido": lifestore_products [10][1] , "2º menos vendido" : lifestore_products [17][1] , "3º menos vendido":lifestore_products [27][1], "4º menos vendido": lifestore_products [32][1], "5º menos vendido": lifestore_products [45][1]}
print(Top_5_productos_menores_ventas_marzo)

#
Consigna_ventas_abr = """

A continuación el desplegado total de todas las ventas en ABRIL 

"""

print(Consigna_ventas_abr)

Ventas_abril = []

for venta in lifestore_sales:
    fecha_venta_abril = venta [3]
    if meses [3] in fecha_venta_abril:
       Ventas_abril.append(venta)
print(Ventas_abril)

print("El total de ventas en el mes fue: ", len(Ventas_abril))

print( """
IDs vendidos en el mes
""")

ids_abril = []

for venta in Ventas_abril:
    id=venta[1]
    ids_abril.append(id)
print(ids_abril)

Top5max_ventas_abril = """

Los 5 productos más vendidos en abril
"""

print(Top5max_ventas_abril)

Top_5_productos_mayores_ventas_abr = {"Más vendido": lifestore_products [2][1] , "2º más vendido" : lifestore_products [53][1] , "3º más vendido":lifestore_products [4][1], "4º más vendido": lifestore_products [41][1], "5º más vendido": lifestore_products [3][1]}
print(Top_5_productos_mayores_ventas_abr)


Top5min_ventas_abr = """

Los 5 productos menos vendidos en abril
"""
print(Top5min_ventas_abr)

Top_5_productos_menores_ventas_abr = {"Menos vendido": lifestore_products [7][1] , "2º menos vendido" : lifestore_products [10][1] , "3º menos vendido":lifestore_products [12][1], "4º menos vendido": lifestore_products [20][1], "5º menos vendido": lifestore_products [21][1]}
print(Top_5_productos_menores_ventas_abr)

#
Consigna_ventas_may = """

A continuación el desplegado total de todas las ventas en MAYO 

"""

print(Consigna_ventas_may)

Ventas_may = []

for venta in lifestore_sales:
    fecha_venta_may = venta [3]
    if meses [4] in fecha_venta_may:
       Ventas_may.append(venta)
print(Ventas_may)

print("El total de ventas en el mes fue: ", len(Ventas_may))

print( """
IDs vendidos en el mes
""")

ids_mayo = []

for venta in Ventas_may:
    id=venta[1]
    ids_mayo.append(id)
print(ids_mayo)


Top5max_ventas_may = """

Los 5 productos más vendidos en mayo
"""

print(Top5max_ventas_may)

Top_5_productos_mayores_ventas_may = {"Más vendido": lifestore_products [53][1] , "2º más vendido" : lifestore_products [4][1] , "3º más vendido":lifestore_products [41][1], "4º más vendido": lifestore_products [2][1], "5º más vendido": lifestore_products [56][1]}
print(Top_5_productos_mayores_ventas_may)


Top5min_ventas_may = """

Los 5 productos menos vendidos en mayo
"""
print(Top5min_ventas_may)

Top_5_productos_menores_ventas_may = {"Menos vendido": lifestore_products [5][1] , "2º menos vendido" : lifestore_products [9][1] , "3º menos vendido": lifestore_products[11][1], "4º menos vendido": lifestore_products [28][1], "5º menos vendido": lifestore_products [39][1]}
print(Top_5_productos_menores_ventas_may)

#
Consigna_ventas_jun = """

A continuación el desplegado total de todas las ventas en JUNIO 

"""

print(Consigna_ventas_jun)

Ventas_jun = []

for venta in lifestore_sales:
    fecha_venta_jun = venta [3]
    if meses [5] in fecha_venta_jun:
       Ventas_jun.append(venta)
print(Ventas_jun)

print("El total de ventas en el mes fue: ", len(Ventas_jun))

print( """
IDs vendidos en el mes
""")

ids_junio = []

for venta in Ventas_jun:
    id=venta[1]
    ids_junio.append(id)
print(ids_junio)


Top5max_ventas_jun = """

Los 5 productos más vendidos en junio
"""

print(Top5max_ventas_jun)

Top_5_productos_mayores_ventas_jun = {"Más vendido": lifestore_products [1][1] , "2º más vendido" : lifestore_products [3][1]}


Top5min_ventas_jun = """

Los 5 productos menos vendidos en junio
"""
print(Top5min_ventas_jun)

Top_5_productos_menores_ventas_jun = {"Menos vendido": lifestore_products [1][1] , "2º menos vendido" : lifestore_products [6][1] , "3º menos vendido":lifestore_products [10][1], "4º menos vendido": lifestore_products [17][1], "5º menos vendido": lifestore_products [46][1]}
print(Top_5_productos_menores_ventas_jun)

#
Consigna_ventas_jul = """

A continuación el desplegado total de todas las ventas en JULIO 

"""

print(Consigna_ventas_jul)

Ventas_jul = []

for venta in lifestore_sales:
    fecha_venta_jul = venta [3]
    if meses [6] in fecha_venta_jul:
       Ventas_jul.append(venta)
print(Ventas_jul)

print("El total de ventas en el mes fue: ", len(Ventas_jul))

print( """
IDs vendidos en el mes
""")

ids_julio = []

for venta in Ventas_jul:
    id=venta[1]
    ids_julio.append(id)
print(ids_julio)


Top5max_ventas_jul = """

Los 5 productos más vendidos en julio
"""

print(Top5max_ventas_jul)

Top_5_productos_mayores_ventas_jul = {"Más vendido": lifestore_products [0][1] , "2º más vendido" : lifestore_products [2][1] , "3º más vendido":lifestore_products [53][1]}
print(Top_5_productos_mayores_ventas_jul)


Top5min_ventas_jul = """

Los 5 productos menos vendidos en julio
"""
print(Top5min_ventas_jul)

Top_5_productos_menores_ventas_jul = {"Menos vendido": lifestore_products [4][1] , "2º menos vendido" : lifestore_products [6][1] , "3º menos vendido":lifestore_products [41][1], "4º menos vendido": lifestore_products [46][1]}
print(Top_5_productos_menores_ventas_jul)

#
Consigna_ventas_ago = """

A continuación el desplegado total de todas las ventas en AGOSTO 

"""

print(Consigna_ventas_ago)

Ventas_ago = []

for venta in lifestore_sales:
    fecha_venta_ago = venta [3]
    if meses [7] in fecha_venta_ago:
       Ventas_ago.append(venta)
print(Ventas_ago)

print("El total de ventas en el mes fue: ", len(Ventas_ago))

print( """
IDs vendidos en el mes
""")

ids_agosto = []

for venta in Ventas_ago:
    id=venta[1]
    ids_agosto.append(id)
print(ids_agosto)

Top5max_ventas_ago = """

Los 5 productos más vendidos en agosto
"""

print(Top5max_ventas_ago)

Top_5_productos_mayores_ventas_ago = {"Más vendido": lifestore_products [53][1]}
print(Top_5_productos_mayores_ventas_ago)


Top5min_ventas_ago = """

Los 5 productos menos vendidos en agosto
"""
print(Top5min_ventas_ago)

Top_5_productos_menores_ventas_ago = {"Menos vendido": lifestore_products [47][1]}
print(Top_5_productos_menores_ventas_ago)

#
Consigna_ventas_sep = """

A continuación el desplegado total de todas las ventas en SEPTIEMBRE 

"""

print(Consigna_ventas_sep)

Ventas_sep = []

for venta in lifestore_sales:
    fecha_venta_sep = venta [3]
    if meses [8] in fecha_venta_sep:
       Ventas_sep.append(venta)
print(Ventas_sep)

print("El total de ventas en el mes fue: ", len(Ventas_sep))

print( """
IDs vendidos en el mes
""")

ids_septiembre = []

for venta in Ventas_sep:
    id=venta[1]
    ids_septiembre.append(id)
print(ids_septiembre)


Top5max_ventas_sep = """

Los 5 productos más vendidos en septiembre
"""

print(Top5max_ventas_sep)

Top_5_productos_mayores_ventas_sep = {"Más vendido": lifestore_products [16][1]}
print(Top_5_productos_mayores_ventas_sep)


Top5min_ventas_sep = """

Los 5 productos menos vendidos en septiembre
"""
print(Top5min_ventas_sep)

print ("NO SE PRESENTARON VENTAS EN EL MES")

#
Consigna_ventas_oct = """

A continuación el desplegado total de todas las ventas en OCTUBRE 

"""

print(Consigna_ventas_oct)

print ("NO SE PRESENTARON VENTAS EN EL MES")

Ventas_oct = []

for venta in lifestore_sales:
    fecha_venta_oct = venta [3]
    if meses [9] in fecha_venta_oct:
       Ventas_oct.append(venta)
print(Ventas_oct)

print("El total de ventas en el mes fue: ", len(Ventas_oct))


print( """
IDs vendidos en el mes
""")

ids_octubre = []

for venta in Ventas_oct:
    id=venta[1]
    ids_octubre.append(id)
print(ids_octubre)

Top5max_ventas_oct = """

Los 5 productos más vendidos en octubre
"""

print(Top5max_ventas_oct)

Top_5_productos_mayores_ventas_oct = {"Más vendido": "xx" , "2º más vendido" : "xx" , "3º más vendido":"xx", "4º más vendido": "xx", "5º más vendido": "xx"}
print(Top_5_productos_mayores_ventas_oct)


Top5min_ventas_oct = """

Los 5 productos menos vendidos en octubre
"""
print(Top5min_ventas_oct)

Top_5_productos_menores_ventas_oct = {"Menos vendido": "xx" , "2º menos vendido" : "xx" , "3º menos vendido":"xx", "4º menos vendido": "xx", "5º menos vendido": "xx"}
print(Top_5_productos_menores_ventas_oct)

#
Consigna_ventas_nov = """

A continuación el desplegado total de todas las ventas en NOVIEMBRE 

"""

print(Consigna_ventas_nov)

print ("NO SE PRESENTARON VENTAS EN EL MES")

Ventas_nov = []

for venta in lifestore_sales:
    fecha_venta_nov = venta [3]
    if meses [10] in fecha_venta_nov:
       Ventas_nov.append(venta)
print(Ventas_nov)

print("El total de ventas en el mes fue: ", len(Ventas_nov))

print( """
IDs vendidos en el mes
""")

ids_noviembre = []

for venta in Ventas_nov:
    id=venta[1]
    ids_noviembre.append(id)
print(ids_noviembre)

Top5max_ventas_nov = """

Los 5 productos más vendidos en noviembre
"""

print(Top5max_ventas_nov)

Top_5_productos_mayores_ventas_nov = {"Más vendido": "xx" , "2º más vendido" : "xx" , "3º más vendido":"xx", "4º más vendido": "xx", "5º más vendido": "xx"}
print(Top_5_productos_mayores_ventas_nov)


Top5min_ventas_nov = """

Los 5 productos menos vendidos en noviembre
"""
print(Top5min_ventas_nov)

Top_5_productos_menores_ventas_nov = {"Menos vendido": "xx" , "2º menos vendido" : "xx" , "3º menos vendido":"xx", "4º menos vendido": "xx", "5º menos vendido": "xx"}
print(Top_5_productos_menores_ventas_nov)

#
Consigna_ventas_dic = """

A continuación el desplegado total de todas las ventas en DICIEMBRE 

"""

print(Consigna_ventas_dic)

print ("NO SE PRESENTARON VENTAS EN EL MES")

Ventas_dic = []

for venta in lifestore_sales:
    fecha_venta_dic = venta [3]
    if meses [11] in fecha_venta_dic:
       Ventas_dic.append(venta)
print(Ventas_dic)

print("El total de ventas en el mes fue: ", len(Ventas_dic))

print( """
IDs vendidos en el mes
""")

ids_diciembre = []

for venta in Ventas_dic:
    id=venta[1]
    ids_diciembre.append(id)
print(ids_diciembre)

Top5max_ventas_dic = """

Los 5 productos más vendidos en diciembre
"""

print(Top5max_ventas_dic)

Top_5_productos_mayores_ventas_dic = {"Más vendido": "xx" , "2º más vendido" : "xx" , "3º más vendido":"xx", "4º más vendido": "xx", "5º más vendido": "xx"}
print(Top_5_productos_mayores_ventas_dic)


Top5min_ventas_dic = """

Los 5 productos menos vendidos en dic
"""
print(Top5min_ventas_dic)

Top_5_productos_menores_ventas_dic = {"Menos vendido": "xx" , "2º menos vendido" : "xx" , "3º menos vendido":"xx", "4º menos vendido": "xx", "5º menos vendido": "xx"}
print(Top_5_productos_menores_ventas_dic)



Consigna1_parte2 = """

CONSIGNA #1 PARTE 2
A continuación verás el número total de busquedas por cada ID product en todo el año en LIFESTORE

"""
print(Consigna1_parte2)

bus_ID=[]
for l in lifestore_searches:
    bus_ID.append(l[1])

n_bus_ID={}
for b in range (1,97):
    n_bus_ID[b]=bus_ID.count(b) 
print(n_bus_ID)

#Muy parecido a las funciones de arriba, para sacar el TOP 10 de las búsquedas apliqué una funcion for y apliqué los conocimientos investigados. 

Consigna1_parte2_1 = """ 

A continuación verás el TOP 10 de los productos más buscados en todo el año en LIFESTORE. El número de la izq es el ID product, el de la derecha es el # de búsquedas  

"""
print(Consigna1_parte2_1)

n_bus_ID_sort=sorted(n_bus_ID.items(), key=operator.itemgetter(1), reverse=True)

top_10=[]
for n in range(0,11):
    top_10.append(n_bus_ID_sort[n])
print(top_10)

#En este apartado comencé a hacer un listado de los productos que el documento solicitó para hacer el TOP 5 de productos mejor y peor calificados. El documento decía que se considerara a los productos con devolución, es por eso que no apliqué discriminación de productos.

Consigna2 = """

En las siguientes listas podrás ver los 5 productos mejores calificados así como los peores calificados
(Este listado incluye los productos con devolución y excluye a los que no tienen reseñas"""

# Apartado para la lista del Top 5 de productos con mejores y peores reseñas. 

C2_p1 = """ 

CONSIGNA #2 

Aquí podrás ver el listado del TOP 5 de los productos con las MEJORES reseñas, considerando los productos con devolución, tal y como lo indica el documento

"""
print(C2_p1)


mejores_calificados = 5
prod_mejores_calificados = []

for producto in lifestore_sales:
    prod_5_estre = producto [2]
    if prod_5_estre == mejores_calificados:
       prod_mejores_calificados.append(producto)

#print (prod_mejores_calificados)
#print(len(prod_mejores_calificados))


prod_top5 = []
for prod in prod_mejores_calificados:
    id = prod [1]
    prod_top5.append(id)
#print(prod_top5)

n_prod_top5={}
for p in range(1,86):
    n_prod_top5[p]=prod_top5.count(p)

#print(n_prod_top5)

n_prod_top5_sort=sorted(n_prod_top5.items(), key=operator.itemgetter(1), reverse=True)

top_5_reseñas=[]
for n in range(0,5):
    top_5_reseñas.append(n_prod_top5_sort[n])

print(top_5_reseñas)


C2_p2 = """ 

Aquí podrás ver el listado del TOP 5 de los productos con las PEORES reseñas, considerando los productos con devolución, tal y como lo indica el documento

"""
print(C2_p2)


peor_calificados_3 = 3
peor_calificados_2 = 2
peor_calificados_1 = 1 
prod_peor_calificados = []

for producto in lifestore_sales:
    prod_3_estre = producto [2]
    prod_2_estre = producto [2]
    prod_1_estre = producto [2]
    if prod_3_estre == peor_calificados_3: 
        prod_peor_calificados.append(producto)
    elif prod_2_estre == peor_calificados_2:
        prod_peor_calificados.append(producto)
    elif prod_1_estre == peor_calificados_1: 
       prod_peor_calificados.append(producto)

#print (prod_peor_calificados)
#print(len(prod_peor_calificados))


prod_top5_peor = []
for prod in prod_peor_calificados:
    id = prod [1]
    prod_top5_peor.append(id)
#print(prod_top5)

n_prod_top5_peor={}
for p in range(1,86):
    n_prod_top5_peor[p]=prod_top5_peor.count(p)

#print(n_prod_top5)

n_prod_top5_peor_sort=sorted(n_prod_top5_peor.items(), key=operator.itemgetter(1), reverse=True)

top_5_reseñas_peor=[]
for n in range(0,5):
    top_5_reseñas_peor.append(n_prod_top5_peor_sort[n])

print(top_5_reseñas_peor)


Consigna3 = """

CONSIGNA #3

En las siguientes listas podrás ver el total de ventas por mes y a nivel anual

"""

print(Consigna3)

Lista_de_precios = []

for venta in lifestore_products:
    precio = venta [2]
    Lista_de_precios.append(precio)


#No supé sacar la relación entre ID y precio, para hacer la suma mediante código :( De verdad que lo inteté, pero no me salió. Es un punto que me gustaría revisar en tutoría.)


print("El total de ventas en enero fue: $119,607.00")
print("El total de ventas en febrero fue: $110.139,00")
print("El total de ventas en marzo fue: $164.729,00")
print("El total de ventas en abril fue: $193.295,00")
print("El total de ventas en mayo fue: $96.394,00")
print("El total de ventas en junio fue: $36.949,00")
print("El total de ventas en julio fue: $26.949,00")
print("El total de ventas en agosto fue: $3.077,00")
print("El total de ventas en septiembre fue: $4.199,00")
print("El total de ventas en octubre fue: $00.0")
print("El total de ventas en noviembre fue: $00.0")
print("El total de ventas en diciembre fue: $00.0")

print("Eltotal de ventas a nivel anual fue: $755.338,00")


print("Los meses con mayor cantidad de ventas: Abril, Marzo y Enero")


print("Fin del informe")
