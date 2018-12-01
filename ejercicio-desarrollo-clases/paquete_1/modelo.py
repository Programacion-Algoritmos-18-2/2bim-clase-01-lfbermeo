#clase principal
class Persona(object):
    """
    """
    
    def __init__(self, n, n_1, n_2, n_3):
        """
        """
        #atributos de la clase asigandole a nota que su tipo de valor es float
        self.nombre = n
        self.nota1 = float(n_1) 
        self.nota2 = float(n_2)
        self.nota3 = float(n_3)
#metodos agregar y obtener para cada uno de los atributos
    def agregar_nombre(self, n):
        """
        """
        self.nombre = n

    def obtener_nombre(self):
        """
        """
        return self.nombre

    def agregar_nota1(self, n_1):
        """
        """
        self.nota1 = float(n_1)

    def obtener_nota1(self):
        """
        """
        return self.nota1
    
    def agregar_nota2(self, n_2):
        """
        """
        self.nota2 = float(n_2)    

    def obtener_nota2(self):
        """
        """
        return self.nota2
    def agregar_nota3(self, n_3):
        """
        """
        self.nota3 = float(n_3)

    def obtener_nota3(self):
        """
        """
        return self.nota3
#calculo del pormedio general para cada uno de los alumnos
    def obtener_promedio(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3
 #metodo el cuál enviamos a imprimir   
    def __str__(self):
        return "\nNombre alumno:%s\nPromedio alumno:%f" % (self.nombre, self.obtener_promedio())