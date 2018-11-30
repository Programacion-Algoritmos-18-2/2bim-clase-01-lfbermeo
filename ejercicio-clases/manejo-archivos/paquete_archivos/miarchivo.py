
import codecs

class MiArchivo:
    """
    """
    
    def __init__(self):
        """
        """
        #"data..."hace referencia la ruta del archico y con "r" lo lee
        self.archivo = codecs.open("data/demo.csv", "r")

    def obtener_informacion(self):
        #readlines retorn los valores de archivo y las corre
        return self.archivo.readlines()

    def cerrar_archivo(self):
        #cierra el programa
        self.archivo.close()


class MiArchivoEscribir:
    """
    """
    
    def __init__(self):
        """
        """
        self.archivo = codecs.open("data/demo2.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write("%s-%s-%d-%d\n" % (p.nombre, p.apellido,\
                p.edad, p.codigo))

    def cerrar_archivo(self):
        self.archivo.close()
