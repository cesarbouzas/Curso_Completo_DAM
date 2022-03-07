# -*- coding: utf-8 -*- 
'''
Created on 20 de ene. de 2016

'''
#Definición
IVal1 = ["valor1", 2, 2 + 4j] 
print "Lista:", IVal1
print "Lista valor con índice 2 d[2]:", IVal1[2]

#Es dinámico 
IVal1.append(6 + 7j) 
print "Lista añadir:", IVal1 
IVal1[3] = "Mi cadena" 
print "Lista modificar:", IVal1 
del IVal1[0] # Base cero 
print "Lista borrar:", IVal1

#Se puede conseguir partes
print "Desde el final Índice negativo", IVal1[-2] # -1 es el último
print "Una parte", IVal1[1:] #desde el segundo hasta el final, empezamos en cero
print "Una parte", IVal1[1:2] # inicio incluido Índice fin excluido

#Operadores +,+=,*
print "Dos listas:", IVal1 + IVal1 
print "Una lista tres veces:", IVal1 * 3 
IVal2 = [True] 
IVal2 += IVal1
print "+=", IVal2


#Funciones básicas
print "    Funciones básicas    "
print IVal1 
print len(IVal1)
print IVal1.index(2 + 4j) #índice del valor 2+4j
print 3 in IVal1 # ¿3 está en la lista?
print IVal1.remove(2) # borramos por valor, no por índice
print IVal1
print IVal1.pop() # Extrae el último, no tiene parámetro 
print IVal1
print IVal1.insert(len(IVal1), "45") # Insertamos en la posición final 
print IVal1
print IVal1.extend([1, 2, 3]) # Insertamos todos los del objeto iterable (en este caso la lista [1,2,3]) 
print IVal1
