def get_list(doc):
    f = open(doc, mode="rt", encoding="utf-8")
    lista_lineas = f.readlines()
    lista_palabras = split_lineas(lista_lineas)
    dic_palabras = {}
    for palabra in lista_palabras:
        for i in palabra:
            if dic_palabras.get(len(i)) != i:
                if dic_palabras.get(len(i)) != None:
                    aux = dic_palabras.get(len(i))
                    aux = str(aux) + ", " + i
                else:
                    dic_palabras[len(i)] = i
                    print(dic_palabras)
      
        


        

def split_lineas(lineas):
    palabras = []
    for linea in lineas:
        palabras.append(linea.split(" "))
        return palabras

get_list("doc_pruebas.txt")