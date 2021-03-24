from libro import *


def get_list(doc):
    f = open(doc, mode="rt", encoding="utf-8")
    lista_lineas = f.readlines()
    lista_palabras = split_lineas(lista_lineas)
    #print(lista_palabras)
    dic_palabras = {}
    if len(lista_palabras) == 0:
        raise ValueError("El fichero no tiene ninguna linea")
    else:
        for palabra in lista_palabras:
            for i in palabra:
                if dic_palabras.get(len(i)) != i:
                    
                    if dic_palabras.get(len(i)) != None:
                        
                        aux = dic_palabras.get(len(i))
                        aux = str(aux) + ", " + i
                        dic_palabras[len(i)] = aux
                    else:
                        dic_palabras[len(i)] = i
        
      
        


        

def split_lineas(lineas):
    palabras = []
    for linea in lineas:
        
        palabras.append(linea.split(" "))
        
    return palabras


def mas_antiguos( lista_libros, anyo):
    lista_titulos = []
    if anyo < 1900:
        raise ValueError("El año ha de ser mayor a 1900")
    elif anyo > 2021:
        raise ValueError("El año ha de ser menor que 2021")

    else:
        for i in range(len(lista_libros)):
            if (lista_libros[i].get_anyo() == anyo) or (lista_libros[i].get_anyo()+1 ==anyo):
                lista_titulos.append(lista_libros[i].get_titulo())
        return lista_titulos




libros = []
libro1 = Libro("Pepe", "Hola Mundo", 1950)
libros.append(libro1)
libro2 = Libro("Carlos", "Adios Mundo", 1900)
libros.append(libro2)
libro3 = Libro("Ana", "Hola Playa", 1949)
libros.append(libro3)
libro4 = Libro("Maria", "Lorem ipsum", 1951)
libros.append(libro4)

lista_antiguos= mas_antiguos(libros,1950)
print(str(lista_antiguos))

get_list("doc_pruebas.txt")