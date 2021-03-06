# -*- coding: utf-8 -*-
# comparación de clases
class Mueble:  # el primer parámetro siempre self en todos
    def __init__(self, tipo):  # Constructor el destructor es __del(self)
        self.tipo = tipo

    def getTipo(self):  # método getter
        return self.tipo

    def setTipo(self, tipo):  # método setter
        self.tipo = tipo

    # ver http://docs.python.org/2/reference/datamodel.html para todas las opciones

    # Personalización de las clases
    def __cmp__(self, other):
        if self.getTipo() < other.getTipo():
            return -1
        elif self.getTipo() == other.getTipo():
            return 0
        else:
            return 1

    def __str__(self):
        return "El objeto vale: " + str(self.tipo)

    def __len__(self):
        return self.tipo.__sizeof__()


muVal1 = Mueble(3)
muVal2 = Mueble(2)
muVal3 = Mueble(3)

if muVal1 == muVal2:
    print "Iguales"
else:
    print "distintos"

if muVal1 == muVal1:
    print "Iguales"
else:
    print "distintos"

if muVal1 == muVal3:  # ¿contienen el mismo valor?
    print "Iguales"
else:
    print "distintos"

if muVal1 is muVal3:  # ¿es el mismo objeto?
    print "Iguales"
else:
    print "distintos"

print muVal1
print len(muVal1)
