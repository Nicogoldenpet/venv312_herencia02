#Importando los módulos y colorama
import Modules.clases as clases
import Modules.functions as functions
from colorama import Fore,init, just_fix_windows_console

init()
just_fix_windows_console()

def main(produ1, produ2, produ3): #Definiendo la función main()
    functions.ingreso()
    functions.registro(produ1, produ2, produ3)

if __name__ == "__main__": #Ejecutando el código con las instancias de las clases
    produ1 = clases.ProductoImpreso()
    produ2 = clases.ProductoGrabado()
    produ3 = clases.ProductoSoftware()
    main(produ1, produ2, produ3)

    
    