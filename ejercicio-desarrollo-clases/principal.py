#realizamos la importación
from paquete_archivo.miArchivo import MiArchivo,MiArchivoEscribir
from paquete_1.modelo import Persona
#creamos  dos objetos
m = MiArchivo()
m2 = MiArchivoEscribir()

#obtenemos la información 
lista = m.obtener_informacion()
#recorremos la lista
lista = [l.split("|") for l in lista]

#hacemos referencia que toma los valores desde la posición 1
lista = lista[1:]
#recorremos la lista
for d in lista:
    p = Persona(d[0], d[1], d[2], d[3])
    #imprimimos
    print(p)
    m2.agregar_informacion(p)
#cerramos los archivos
m.cerrar_archivo()
m2.cerrar_archivo()

