from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona

m = MiArchivo()
lista = m.obtener_informacion()
#no se debe imprimir "|" este caracter 
lista = [l.split("|") for l in lista]

# print(lista)
#[1:] desde la posiicon 1 en adelante
lista = lista[1:]
#imprime la primer linea
#p= Persona (lista [1][1], lista[1][2], lista[1][3], lista[1][0])

for d in lista:
    #print(d)
    p = Persona(d[1], d[2], d[3], d[0])
    print(p)
