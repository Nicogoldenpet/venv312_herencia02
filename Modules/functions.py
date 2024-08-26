#Importando los módulos y las librerias
import msvcrt
import platform
import os
import time
import random
from colorama import Fore,init, just_fix_windows_console
import Modules.clases as clases
init()
just_fix_windows_console()


def ingreso(): #Definiendo la función de ingreso
    print(Fore.LIGHTBLUE_EX)
    print("+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    print("|                                                                                                                                                                                                                                         |")
    print("|                                                                                                                                                                                                                                         |")
    print("|                                                                                            BIENVENIDO AL PROGRAMA DE HERENCIAS #2                                                                                                         |")
    print("|                                                                                            PARA INGRESAR PRESIONE CUALQUIER TECLA                                                                                                       |")
    print("|                                                                                                                                                                                                                                         |")
    print("|                                                                                                                                                                                                                                         |")
    print("+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+")
    msvcrt.getch()
    limpiar_pantalla()
    

def limpiar_pantalla(): #Definiendo la función para limpiar pantalla
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def registro(produ1, produ2, produ3): #Definiendo la función de registro de los productos 

    produ1.set__titulo(input("Ingrese el nombre del producto: ")) #Registrando el nombre del producto
    produ1.set__autor(input("Ingrese el autor del producto: ")) #Registrando el autor del producto

    codigo = None
    while codigo is None:
        try:
            print(Fore.LIGHTBLUE_EX)
            codigo = int(input("Ingrese el código de barras del producto: ")) #Registrando el código (Unicamente con números)
        except ValueError:
            print(Fore.LIGHTYELLOW_EX)
            print("Solo se aceptan números.")

    produ1.set__codigo(codigo)

    tipo = None
    while tipo != "1" and tipo != "2" and tipo != "3": #El usuario podrá seleccionar unicamente tres opciones para registrar el tipo de produto
        print(Fore.LIGHTBLUE_EX, "¿Qué producto desea registrar?: 1. PRODUCTO IMPRESO / 2. PRODUCTO GRABADO / 3. PRODUCTO SOFTWARE")
        tipo = msvcrt.getwch()

        if tipo == "1":
            print(Fore.LIGHTYELLOW_EX, "Se registrará un PRODUCTO IMPRESO") #Ingresando a la sección Producto Impreso
            time.sleep(2)
            limpiar_pantalla() #Limpiando la terminal

            print(Fore.LIGHTBLUE_EX)
            produ1.set__editorial(input("Ingrese la editorial: ")) #Registrando la editorial
            produ1.set__año(input("Ingrese el año de lanzamiento del producto: ")) #Registrando el año de lanzamiento del producto

            precio = None
            while precio is None:
                try:
                    print(Fore.LIGHTBLUE_EX)
                    precio = int(input("Ingrese el precio del producto: ")) #Registrando el precio del producto (Unicamente con números)
                except ValueError:
                    print(Fore.LIGHTYELLOW_EX)
                    print("Solo se aceptan números.")

            produ1.set__precio(precio)

            impreso = None
            while impreso != "1" and impreso != "2": #El usuario podrá seleccionar unicamente dos opciones para definir el producto impreso
                print(Fore.LIGHTBLUE_EX, "¿Cuál es el producto impreso? 1. REVISTA / 2. LIBRO")
                impreso = msvcrt.getwch()

                if impreso == "1":
                    actividad = ["EN VENTA", "AGOTADA", "INEXISTENTE", "POCAS UNIDADES"] #Definiendo los estados en una lista
                    print(Fore.LIGHTYELLOW_EX, "El producto impreso es REVISTA...") #Ingresando a la sección REVISTA
                    time.sleep(2)
                    limpiar_pantalla() #Limpiando la terminal
                    
                    print(Fore.LIGHTBLUE_EX)
                    product = clases.Revista( #Instanciando una clase con todos los datos
                        codigo=produ1.get__codigo(),
                        titulo=produ1.get__titulo(),
                        autor=produ1.get__autor(),
                        editorial=produ1.get__editorial(),
                        año=produ1.get__año(),
                        precio=produ1.get__precio(),
                        volumen=input("Ingrese el volumen de la revista: "),
                        labor = random.choice(actividad) #Definiendo un estado aleatorio con random.choice()
                    )
                    product.informacion() #Llamando la función para mostrar la información
                    break #Cerrando el código
    

                elif impreso == "2":
                    actividad = ["EN VENTA", "AGOTADO", "INEXISTENTE", "POCAS UNIDADES"] #Definiendo los estados en una lista
                    print(Fore.LIGHTYELLOW_EX, "El producto impreso es LIBRO...") #Ingresando a la sección LIBRO
                    time.sleep(2)
                    limpiar_pantalla() #Limpiando la terminal

                    print(Fore.LIGHTBLUE_EX)
                    product = clases.Libro( #Instanciando una clase con todos los datos
                        codigo=produ1.get__codigo(),
                        titulo=produ1.get__titulo(),
                        autor=produ1.get__autor(),
                        editorial=produ1.get__editorial(),
                        año=produ1.get__año(),
                        precio=produ1.get__precio(),
                        idioma=input("Ingrese el idioma del libro: "),
                        labor = random.choice(actividad) #Definiendo un estado aleatorio con random.choice()
                    )
                    product.informacion() #Llamando la función para mostrar la información
                    break #Cerrando el código

                else:
                    print(Fore.LIGHTYELLOW_EX)
                    print("Carácter no válido.")
    
        elif tipo == "2":
            actividad = ["EN VENTA", "AGOTADO", "INEXISTENTE", "POCAS UNIDADES"] #Definiendo los estados en una lista
            print(Fore.LIGHTYELLOW_EX, "Se registrará un PRODUCTO GRABADO") #Ingresando a la sección Producto Grabado
            time.sleep(2)
            limpiar_pantalla() #Limpiando la terminal

            tiempo_duracion = None
            while tiempo_duracion is None:
                try:
                    print(Fore.LIGHTBLUE_EX)
                    tiempo_duracion = int(input("Ingrese la duración del producto grabado (En minutos): ")) #Registrando el duración del producto (Unicamente con números)
                except ValueError:
                    print(Fore.LIGHTYELLOW_EX)
                    print("Solo se aceptan números.")

            product = clases.ProductoGrabado( #Instanciando una clase con todos los datos
                codigo=produ1.get__codigo(),
                titulo=produ1.get__titulo(),
                autor=produ1.get__autor(),
                tiempo_duracion=tiempo_duracion,
                medio_tecno=input("¿Cuál es el medio tecnológico del producto?: "), #Registrando el medio tecnológico del producto
                labor = random.choice(actividad) #Definiendo un estado aleatorio con random.choice()
            )
            product.informacion() #Llamando la función para mostrar la información
            break #Cerrando el código

        elif tipo == "3":
            actividad = ["EN VENTA", "AGOTADO", "INEXISTENTE", "POCAS UNIDADES"] #Definiendo los estados en una lista
            print(Fore.LIGHTYELLOW_EX, "Se registrará un PRODUCTO SOFTWARE") #Ingresando a la sección Producto Software
            time.sleep(2)
            limpiar_pantalla() #Limpiando la terminal

            sistema_operativo = None
            while sistema_operativo is None:
                try:
                    print(Fore.LIGHTBLUE_EX)
                    sistema_operativo = int(input("Ingrese la versión del sistema operativo: ")) #Registrando el sistema operativo del producto (Unicamente con números)
                except ValueError:
                    print(Fore.LIGHTYELLOW_EX)
                    print("Solo se aceptan números.")

            product = clases.ProductoSoftware( #Instanciando una clase con todos los datos
                codigo=produ1.get__codigo(),
                titulo=produ1.get__titulo(),
                autor=produ1.get__autor(),
                sistema_operativo=sistema_operativo,
                version=input("Ingrese la versión del software: "), #Registrando la versión del software
                labor = random.choice(actividad) #Definiendo un estado aleatorio con random.choice()
            )
            product.informacion() #Llamando la función para mostrar la información
            break #Cerrando el código

        else:
            print(Fore.LIGHTYELLOW_EX)
            print("Carácter no válido.")

