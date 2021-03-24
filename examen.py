def get_list(doc):
    f = open(doc, mode="rt", encoding="utf-8")
    lista_lineas = f.readlines()
    lista_palabras = split_lineas(lista_lineas)
    print(lista_palabras)
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


def mas_antiguos(self, libros, anyo):
    pass



get_list("doc_pruebas.txt")