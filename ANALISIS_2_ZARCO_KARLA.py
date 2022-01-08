#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 12:53:22 2022

@author: karlazarco
"""

import csv
import pandas as pd


#Consigna 1: Determinar el TOP 10 de las rutas más demandadas de Synergy Logistics

"""
Para determinar el Top 10 de las rutas más importantes de Synergy Logistics, se utilizaron
Pandas para trabajar solamente con las columnas necesarias: Origen, destino y 
medio de transporte. 

"""




synergy_dataframe = pd.read_csv('SL_database.csv', index_col=0,
                                encoding='utf-8', 
                                parse_dates=[4, 5])

combinaciones = synergy_dataframe.groupby(by=['origin','destination','transport_mode'])
descripcion = combinaciones.describe()['total_value']
mean = descripcion['count']
mean_sort = mean.sort_values(ascending=False)

import seaborn as sns
import matplotlib.pyplot as plt
mean_sort = mean_sort.to_frame().reset_index()

Con1 = """
A continuación se muestran las 10 rutas más populares de Synergy Logistics en función del 
número de veces que han sido utilizadas, tomando en consideración el medio de transporte utilizado:
""" 

print(Con1)



print(mean_sort[0:10])

#Consigna 2: Determinar los 3 medios de transporte más importantes para Synergy Logistics, considerando el valor de las importaciones y exportanciones.

"""
    Para determinar los medios de transporte que se utilizan en Synergy Logistics: 
    
    1. Se obtuvieron 2 listas, del archivo csv, con los valores necesarios
    para trabajar: Medio de transporte y Valor total de las imp y exp.
    Estas se consiguieron a través de  bucles for que iteraron sobre las columnas
    [7] y [9] del archivo csv, y se fueron guardando en una lista vacia mediante
    la función "append". 
   
    2. Una vez obtenidos los datos de ambas listas, se procedió a aplicar la función
    "set" sobre la lista "medios_transporte" para eliminar los elementos repetidos y 
    así determinar la cantidad total de los medios de transporte de la empresa.
    
    3. Posteriormente, a través de una función "zip" se hizo la agrupación de 
    las listas separadas, de este modo se obtuvo una lista de tuplas con 
    todos los datos acoplados. 
    
    4. Ahora era necesario determinar la suma total del valor de las imp/exp
    de cada medio de transporte, por lo que se procedió a definir un objeto contador 
    en cero al igual que 4 variables correspondientes a los transportes con el mismo número. 
    De este modo, sería posible la iteración y suma en ambas listas. 
    
    5. Al tener el total de los resultados por medio de transporte, finalmente se obtuvó
    un pequeño listado con los elementos acomodados de mayor a menor, esto con una
    función obtenida a través de investigación y consulta externa, pero que tiene el 
    objetivo de ordenar valores de dos listas "unidas"
    
    
    
    """


medios_transporte = []

with open("SL_database.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    for linea in lector:
        if linea [7] == "transport_mode":
            continue
        medios_transporte.append(linea[7])
        
    #print(medios_transporte)

Con2 = """
En esta sección se muestran todos los medios de transporte que utiliza
Synergy Logistics para la ejecución sus servicios de importación y exportación:
""" 

print(Con2)

 
transportes = set(medios_transporte)
print(transportes)
    

valor_total = []

with open("SL_database.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    for linea in lector:
         if linea [9] == "total_value":
             continue
         valor_total.append(int(linea[9]))
         
    #print(valor_total)
    
agrupacion = (zip(valor_total, medios_transporte))
#print(list(agrupacion))

#Conteo de medios de trasporte

c=0
   
air=0
sea=0
rail=0
road=0


for t in medios_transporte:
    if t=='Air':
        air=air+valor_total[c]
    if t=='Sea':
        sea=sea+valor_total[c]
    if t=='Rail':
        rail=rail+valor_total[c]
    if t=='Road':
        road=road+valor_total[c]
    c=c+1
    
totales={
    'Air':air,
    'Sea':sea,
    'Rail':rail,
    'Road':road
    }

Con2_1 = """
El siguiente apartado contiene el valor total de las importaciones/exportaciones
por cada medio de transporte utilizado por Synergy Logistics
"""

print (Con2_1)

print(totales)

sorted_values=sorted(totales.values(),reverse=True)
sorted_dict={}
for i in sorted_values:
    for k in  totales.keys():
        if totales[k]==i:
            sorted_dict[k]=totales[k]
            break

Con2_2 = """
Listado ordenado de mayor a menor de los medios de transporte utilizados por 
Synergy Logistics en función del valor tota de las importaciones/exportaciones
"""

print (Con2_2)

print(sorted_dict)


#Consigna 3: Determinar el grupo de países que le generan el 80% del valor de las importaciones y exportaciones


Con3 = """

Lista de los países que generaron servicios de importación / exportación
"""

print(Con3)

paises = []

with open("SL_database.csv", "r") as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    for linea in lector:
        if linea [2] == "origin":
            continue
        paises.append(linea[2])
        
    #print(paises)
    
    paises_totales = set(paises)
    print(paises_totales)
    #print(len(paises_totales))
    
    
agrupacion_2 = (zip(valor_total, paises))
#print(list(agrupacion_2))

#Conteo de medios de trasporte

c=0
   
Germany=0
France=0
Belgium=0
Spain=0
UnitedArabEmirates=0
Russia=0
Mexico=0
Vietnam=0
Switzerland=0
Malaysia=0
Singapore=0
Netherlands=0
Japan=0
USA=0
UnitedKingdom=0
Canada=0
India=0
Austria=0
Australia=0
Italy=0
SouthKorea=0
Brazil=0
China=0


for t in paises:
    if t=='Germany':
        Germany=Germany+valor_total[c]
    if t=='France':
        France=France+valor_total[c]
    if t=='Belgium':
        Belgium=Belgium+valor_total[c]
    if t=='Spain':
        Spain=Spain+valor_total[c]
    if t=='United Arab Emirates':
        UnitedArabEmirates=UnitedArabEmirates+valor_total[c]
    if t=='Russia':
        Russia=Russia+valor_total[c]
    if t=='Mexico':
        Mexico=Mexico+valor_total[c]
    if t=='Vietnam':
        Vietnam=Vietnam+valor_total[c]
    if t=='Switzerland':
        Switzerland=Switzerland+valor_total[c]
    if t=='Malaysia':
        Malaysia=Malaysia+valor_total[c]
    if t=='Singapore':
        Singapore=Singapore+valor_total[c]
    if t=='Netherlands':
        Netherlands=Netherlands+valor_total[c]
    if t=='Japan':
        Japan=Japan+valor_total[c]
    if t=='USA':
        USA=USA+valor_total[c]
    if t=='United Kingdom':
        UnitedKingdom=UnitedKingdom+valor_total[c]
    if t=='Canada':
        Canada=Canada+valor_total[c]
    if t=='India':
        India=India+valor_total[c]
    if t=='Austria':
        Austria=Austria+valor_total[c]
    if t=='Australia':
        Australia=Australia+valor_total[c]
    if t=='Italy':
        Italy=Italy+valor_total[c]
    if t=='South Korea':
        SouthKorea=SouthKorea+valor_total[c]
    if t=='Brazil':
        Brazil=Brazil+valor_total[c]
    if t=='China':
        China=China+valor_total[c]
    c=c+1
    
totales_2 = {
               
        'Germany':Germany,
        'France':France,
        'Belgium':Belgium,
        'Spain':Spain,
        'United Arab Emirates':UnitedArabEmirates,
        'Russia':Russia,
        'Mexico': Mexico,
        'Vietnam': Vietnam,
        'Switzerland': Switzerland,
        'Malaysia': Malaysia,
        'Singapore': Singapore,
        'Netherlands': Netherlands,
        'Japan': Japan,
        'USA': USA,
        'United Kingdom':UnitedKingdom,
        'Canada': Canada,
        'India': India,
        'Austria': Austria,
        'Australia' : Australia,
        'Italy' : Italy,
        'South Korea' : SouthKorea,
        'Brazil': Brazil,
        'China': China,
        
        }

Con3_1 = """

Listado de países en conjunto con el valor total de importaciones y exportaciones
que han generado durante los últimos 5 años: 
"""
print(Con3_1)
print(totales_2)

sorted_values=sorted(totales_2.values(),reverse=True)
sorted_dict_2={}
for i in sorted_values:
    for k in  totales_2.keys():
        if totales_2[k]==i:
            sorted_dict_2[k]=totales_2[k]
            break
        
Con3_2 = """
Listado ordenado de mayor a menor de los países que han contratado los servicios de Synergy Logistics 
en función del valor tota de las importaciones/exportaciones
"""

print (Con3_2)
        
print(sorted_dict_2)

    
def sumar_lista (lista):
    suma=0
    
    for valor in lista:
        suma+= valor
    
    return suma


Con3_3= """

Valor total de las importaciones como de las exportaciones
"""

print(Con3_3)

print(sumar_lista(valor_total))


    
    
    
    
    
    
    
    
    
    
    
 









