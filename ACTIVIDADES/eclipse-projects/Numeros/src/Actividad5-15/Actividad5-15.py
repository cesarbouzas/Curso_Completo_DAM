# -*- coding: utf-8 -*- 
'''
Created on 20 de ene. de 2016

'''

# Definición sin tipo al asignar, pero obligatorio asignar antes de usar
sVal1 ="Valor"
sVal2 = "Mi cadena \
    Larga pero en varias lineas"
print sVal1,"-------", sVal2
tTupla1 = (1, "ABC", True)
(v1,v2,v3) = tTupla1 
print "Variables v1 ,v2 y v3:", v1, v2, v3

# Cadenas de formato %d,%s,%f
iVal1 = 23
sVal2 = "José"
print "%s tiene %d años" % (sVal2, iVal1)
print "%s tiene %.2f años" % (sVal2, iVal1)

# Entrada de datos
nombre = raw_input("Cómo te llamas?") 
print "Encantado," + nombre # Comprobar la necesidad del espacio al usar +

