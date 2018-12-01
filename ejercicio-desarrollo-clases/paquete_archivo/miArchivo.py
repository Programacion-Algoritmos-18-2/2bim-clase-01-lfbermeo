import codecs

class MiArchivo:
    #Constructor
    def __init__(self):
        #hacemos referencia a donde está ubicado el archivo
        self.archivo = codecs.open("data/informacion.csv", "r")

    #lee la información del archico
    def obtener_informacion(self):
        return self.archivo.readlines()

    #cierra el archivo
    def cerrar_archivo(self):
        self.archivo.close()


class MiArchivoEscribir:
    #Constructor 
    def __init__(self):
        self.archivo = codecs.open("data/informacion2.csv", "a")

    #agregamos informacion
    def agregar_informacion(self, p):
        self.archivo.write("Nombre alumno: %s\nPromedio alumno: %f\n" % (p.nombre, p.obtener_promedio()))

    #cerramos archivo
    def cerrar_archivo(self):
        self.archivo.close()
