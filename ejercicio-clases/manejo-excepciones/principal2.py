"""
Ejemplos de manejo de expeciones
"""
try:
     numero1 = input("Ingrese un número 1:\n")
     numero1 = int(numero1)
     numero2 = input("Ingrese un número 2:\n")
     numero2 = int(numero2)
     operacion = numero1/numero2
     print("El valor de la operacion es: %d"%(operacion))
#Realizar excepciones para el porgrama con la palabra except     
except NameError as e:
    print("Existe un error: %s" % e)

except ValueError as e:
    print("Existe un error (%s): %s" % (e.__class__, e))

except ZeroDivisionError as e:
	print("Existe un error (%s): %s" % (e.__class__, e))   

#Error padre que es exception que es propia de python       
except Exception as e:
 	print("Existe un error (%s): %s" % (e.__class__, e))