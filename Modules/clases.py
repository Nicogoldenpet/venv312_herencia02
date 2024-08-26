class Producto: #Definiendo la clase padre
    def __init__(self,codigo='',titulo='', autor=""): #Método constructor
        self.__codigo=codigo
        self.__titulo=titulo
        self.__autor=autor

    #Métodos getter y setter para los valores
    def get__codigo(self):
        return self.__codigo
    
    def set__codigo(self, value):
        self.__codigo = value
    
    def get__titulo(self):
        return self.__titulo
    
    def set__titulo(self, value):
        self.__titulo=value

    def get__autor(self):
        return self.__autor
    
    def set__autor(self, value):
        self.__autor=value

    def informacion(self): #Mostrando la información con .format
        print( 'El producto se llama {0} hecho por {1}, su código de barras es: {2}'.format(self.get__titulo(), self.get__autor(), self.get__codigo()))

class ProductoImpreso(Producto): #Definiendo la clase hija de Producto(ProductoImpreso)

    def __init__(self,codigo='',titulo='', autor="", editorial="", año="", precio=""): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(codigo, titulo, autor)
        self.__editorial=editorial
        self.__año=año
        self.__precio=precio

    #Métodos getter y setter para los siguientes valores
    def get__editorial(self):
        return self.__editorial
    
    def set__editorial(self, value):
        self.__editorial = value

    def get__año(self):
        return self.__año
    
    def set__año(self, value):
        self.__año = value

    def get__precio(self):
        return self.__precio
    
    def set__precio(self, value):
        self.__precio = value


    def informacion(self): #Mostrando la información con .format
        print( 'El producto se llama {0} hecho por {1}, su código de barras es: {2}. La editorial es {3}, salió en el año {4} y cuesta {5}.'.format(self.get__titulo(), self.get__autor(), self.get__codigo(), 
                                                                                                                                            self.get__editorial(), self.get__año(), self.get__precio()))
        
class Revista(ProductoImpreso): #Definiendo la clase hija de ProductoImpreso(Revista)

    def __init__(self,codigo='',titulo='', autor="", editorial="", año="", precio="", volumen="", labor=""): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(codigo, titulo, autor, editorial, año, precio)
        self.__volumen=volumen
        self.__labor=labor

    #Métodos getter y setter para los siguientes valores
    def get__volumen(self):
        return self.__volumen
    
    def set__volumen(self, value):
        self.__volumen = value

    def get__labor(self):
        return self.__labor
    
    def set__labor(self, value):
        self.__labor = value

    def informacion(self): #Mostrando la información con .format
        tabla = """
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |                                                                                                                                                                                                           |
    |                                                                                         INFORMACIÓN DE LA REVISTA                                                                                         | 
    |___________________________________________________________________________________________________________________________________________________________________________________________________________|
    |                                                                                                                                                                                                           |
    |    Título                   Autor                   Código                   Editorial                   Año                   Precio                   Volumen                   Estado                  |
    |___________________________________________________________________________________________________________________________________________________________________________________________________________|
    """        
        tabla = tabla + "{8:<4} {0:<25}{1:<24}{2:<25}{3:28}{4:<22}${5:<24}{6:<26}{7:<23} {8}".format(self.get__titulo(),
        self.get__autor(), self.get__codigo(), self.get__editorial(), self.get__año(), self.get__precio(), self.get__volumen(), self.get__labor(), "|")
        tabla = tabla + """
    |___________________________________________________________________________________________________________________________________________________________________________________________________________|
        """
        
        print(tabla)


class Libro(ProductoImpreso): #Definiendo la clase hija de ProductoImpreso(Libro)

    def __init__(self,codigo='',titulo='', autor="", editorial="", año="", precio="", idioma="", labor=""): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(codigo, titulo, autor, editorial, año, precio)
        self.__idioma=idioma
        self.__labor=labor

    #Métodos getter y setter para los siguientes valores
    def get__idioma(self):
        return self.__idioma
    
    def set__idioma(self, value):
        self.__idioma = value

    def get__labor(self):
        return self.__labor
    
    def set__labor(self, value):
        self.__labor = value

    def informacion(self): #Mostrando la información con .format
        tabla = """
    +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |                                                                                                                                                                                                           |
    |                                                                                           INFORMACIÓN DEL LIBRO                                                                                           | 
    |___________________________________________________________________________________________________________________________________________________________________________________________________________|
    |                                                                                                                                                                                                           |
    |     Título                   Autor                   Código                   Editorial                   Año                   Precio                   Idioma                   Estado                  |
    |___________________________________________________________________________________________________________________________________________________________________________________________________________|
    """        
        tabla = tabla + "{8:<5} {0:<25}{1:<24}{2:<25}{3:28}{4:<22}${5:<24}{6:<25}{7:<23} {8}".format(self.get__titulo(),
        self.get__autor(), self.get__codigo(), self.get__editorial(), self.get__año(), self.get__precio(), self.get__idioma(), self.get__labor(), "|")
        tabla = tabla + """
    |___________________________________________________________________________________________________________________________________________________________________________________________________________|
        """
        
        print(tabla)


class ProductoGrabado(Producto): #Definiendo la clase hija de Producto(ProductoGrabado)

    def __init__(self,codigo='',titulo='', autor="", tiempo_duracion="", medio_tecno="", labor=""): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(codigo, titulo, autor)
        self.__tiempo_duracion=tiempo_duracion
        self.__medio_tecno=medio_tecno
        self.__labor=labor

    #Métodos getter y setter para los siguientes valores
    def get__tiempoduracion(self):
        return self.__tiempo_duracion
    
    def set__tiempoduracion(self, value):
        self.__tiempo_duracion = value

    def get__mediotecno(self):
        return self.__medio_tecno
    
    def set__mediotecno(self, value):
        self.__medio_tecno = value

    def get__labor(self):
        return self.__labor
    
    def set__labor(self, value):
        self.__labor = value

    def informacion(self): #Mostrando la información con .format
        tabla = """
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |                                                                                                                                                                                |
    |                                                                        INFORMACIÓN DEL PRODUCTO GRABADO                                                                        | 
    |________________________________________________________________________________________________________________________________________________________________________________|
    |                                                                                                                                                                                |
    |     Título                   Autor                   Código                   Tiempo de duración                   Medio tecnológico                   Estado                  |
    |________________________________________________________________________________________________________________________________________________________________________________|
    """        
        tabla = tabla + "{6:<5} {0:<24} {1:<23} {2:<24} {3:<36} {4:<35} {5:<23} {6}".format(self.get__titulo(),
                                                                                  self.get__autor(), self.get__codigo(), self.get__tiempoduracion(), self.get__mediotecno(), self.get__labor(), "|")
        tabla = tabla + """
    |________________________________________________________________________________________________________________________________________________________________________________|
        """
        
        print(tabla)


class ProductoSoftware(Producto): #Definiendo la clase hija de Producto(ProductoSoftware)

    def __init__(self,codigo='',titulo='', autor="", sistema_operativo="", version ="", labor=""): #Método constructor

        #Añadiendo los datos anteriores a la nueva clase 
        super().__init__(codigo, titulo, autor)
        self.__sistema_operativo=sistema_operativo
        self.__version=version
        
        self.__labor=labor

    #Métodos getter y setter para los siguientes valores
    def get__sistemaoperativo(self):
        return self.__sistema_operativo
    
    def set__sistemaoperativo(self, value):
        self.__sistema_operativo = value

    def get__version(self):
        return self.__version
    
    def set__version(self, value):
        self.__version = value

    def get__labor(self):
        return self.__labor
    
    def set__labor(self, value):
        self.__labor = value

    def informacion(self): #Mostrando la información con .format
        tabla = """
    +--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    |                                                                                                                                                                                |
    |                                                                        INFORMACIÓN DEL PRODUCTO SOFTWARE                                                                       | 
    |________________________________________________________________________________________________________________________________________________________________________________|
    |                                                                                                                                                                                |
    |                Título                   Autor                   Código                   Versión                   Sistema Operativo                   Estado                  |
    |________________________________________________________________________________________________________________________________________________________________________________|
    """        
        tabla = tabla + "{6:<16} {0:<24} {1:<23} {2:<24} {3:<25} {4:<35} {5:<23} {6}".format(self.get__titulo(),
                                                                                  self.get__autor(), self.get__codigo(), self.get__version(), self.get__sistemaoperativo(), self.get__labor(), "|")
        tabla = tabla + """
    |________________________________________________________________________________________________________________________________________________________________________________|
        """
        
        print(tabla)
        

