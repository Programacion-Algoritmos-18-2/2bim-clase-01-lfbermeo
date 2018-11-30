"""
    Ejecutable de manejo de excepciones
"""

from paquete_excepciones.miexepcion import MiError


try:
    x = input("Ingresar valor:\n")
    x = int(x)
    if x < 20:
    	#envia la exception con raise
        raise MiError(x)

except MiError as e:
    print(e)

except ValueError as e:
    print("Existe un error, con el valor (%s) ingresado (%s)" % (x, e))
