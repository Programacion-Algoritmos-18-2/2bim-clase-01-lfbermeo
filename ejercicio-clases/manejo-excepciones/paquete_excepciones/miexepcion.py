"""
    Manejo de Excepciones
"""
#crear expecion siempre que herede de Exception
class MiError(Exception):
    """
    """

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "Error, para el valor ingresado %s" %(self.valor)
