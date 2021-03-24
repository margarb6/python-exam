class Libro:
    """
    Representación de un libro

    Attributes:
        autor (str): Autor del libro
        titulo (str): Titulo del libro
        anyo (int): Año del libro
        
    
    Methods:
        get_anyo(): Devuelve el año del libro
        


    """
    def __init__(self, autor, titulo, anyo):
        self.__autor = autor
        self.__titulo = titulo
        self.__anyo = anyo
    
    def get_anyo(self):
        return self.__anyo

    def get_titulo(self):
        return self.__titulo       