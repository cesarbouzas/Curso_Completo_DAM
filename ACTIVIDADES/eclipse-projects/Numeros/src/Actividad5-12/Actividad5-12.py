# -*- coding: utf-8 -*- 
'''
Created on 18 de ene. de 2016

'''
#Definición
dVal1 ={"key1":"valor1", "key2":"valor2"} 
print "Diccionario:", dVal1
print "Diccionario valor con clave key2 d['key2']:", dVal1['key2']

#Se puede usar cualquier tipo de valor, y en las claves tipos básicos 
dVal2 = {1:"Valor cadena","keyABC":23} 
print "Diccionario:", dVal2
print "Diccionario valor con clave 1 d[1]:", dVal2[1]
print "Diccionario valor con clave keyABC d['keyABC']:", dVal2['keyABC']

#Es dinámico pero sin claves duplicadas 
dVal2[2] = 6 + 7j 
print "Diccionario añadir:", dVal2 
dVal2[2] = "ABC"
print "Diccionario modificar:", dVal2 
del dVal2[1]
print "Diccionario borrar:", dVal2

#Funciones básicas 
print"    Funciones básicas    "
print len(dVal2)
print dVal2.items() #Lista de todo  
print dVal2.keys() #Lista de las claves 
print dVal2.values() #Lista de los valores
print dVal2.has_key("1") # Existe la clave 1. Es una cadena de texto debe dar falso
#dVal2.clear()

print " "
print " "
print " "
print " bucle: "
for item in dVal2:
    print item
    
