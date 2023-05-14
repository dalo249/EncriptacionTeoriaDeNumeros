from encriptacion.modelo import Criptografia


class UIConsola:
    def __init__(self):
        self.criptografia = Criptografia()
        self.mensaje_encriptado: str = ""
        self.opciones: dict = {
            "1": self.generar_ecuacion,
            "2": self.encriptar_mensaje,
            "3": self.calcular_inverso,
            "4": self.desencriptar_mensaje

        }

    def menu(self):
        print("""
        \n
        
        ------------- Menu de opciones -------------
        -----------------Turno PC1------------------
        
        1. Generar la ecuacion secreta   
        2. Encriptar nuevo mensaje     
        
        -----------------Turno PC2------------------
         
        3. Calcular el valor de a y su inverso
        4. Descifrar mensaje
        """)

    def ejecutar(self):
        while True:
            self.menu()
            respuesta: str = str(input("Seleccione una opcion:"))
            opcion = self.opciones.get(respuesta)
            if opcion is None:
                print("La opcion ingresada no es valida, debe ser un numero entre el 1 y 9")
            else:
                opcion()
                input()

    def generar_ecuacion(self):
        print("\nLa ecuacion creada para encriptar tu mensaje es:")
        print("\n+------------------------------+")
        print("           |ECUACION|          ")
        print("+------------------------------+")
        print(self.criptografia.generar_ecuacion())
        print("+------------------------------+")

        print(" |NUMERO ALEATORIO A (INVERSO)|   ")
        print("+------------------------------+")
        print(self.criptografia.a)
        print("+------------------------------+")

        print("      |NUMERO  ALEATORIO B|       ")
        print("+------------------------------+")
        print(self.criptografia.b)
        print("+------------------------------+")

    def encriptar_mensaje(self):
        print("Encriptar mensaje")
        mensaje: str = str(input("Ingrese el mensaje que desee encriptar:"))
        orden: list[int] = self.orden_mensaje_encriptado()
        self.mensaje_encriptado: str = self.criptografia.encriptar_mensaje(mensaje, orden)
        print(self.mensaje_encriptado)

    def orden_mensaje_encriptado(self) -> list[int]:
        print("\nESTRATEGIA ")
        print("\n+---------+---------------+---------------+---------------+")
        print("  |ORDEN|   |POSICION 1|    |POSICION 2|    |POSICION 3|   ")
        print("+---------+---------------+---------------+---------------+")
        print("     1    |      A      | & |     B     | & |    MENSAJE  |")
        print("+---------+---------------+---------------+---------------+")
        print("     2    |      A      | & |  MENSAJE  | & |      B      |")
        print("+---------+---------------+---------------+---------------+")
        print("     3    |      B      | & |     A     | & |    MENSAJE  |")
        print("+---------+---------------+---------------+---------------+")
        print("     4    |      B      | & |  MENSAJE  | & |      A      |")
        print("+---------+---------------+---------------+---------------+")
        print("     5    |   MENSAJE   | & |     A     | & |      B      |")
        print("+---------+---------------+---------------+---------------+")
        print("     6    |   MENSAJE   | & |     B     | & |      A      |")
        print("+---------+---------------+---------------+---------------+")
        opcion: int = int(input("Seleccione la opcion de orden en que desee encriptar el mensaje:"))
        if opcion == 1:
            orden = [0, 1, 2]
            return orden
        elif opcion == 2:
            orden = [0, 2, 1]
            return orden
        elif opcion == 3:
            orden = [1, 0, 2]
            return orden
        elif opcion == 4:
            orden = [1, 2, 0]
            return orden
        elif opcion == 5:
            orden = [2, 0, 1]
            return orden
        elif opcion == 6:
            orden = [2, 1, 0]
            return orden

    def calcular_inverso(self):
        print("Calcular inverso:")
        print(self.mensaje_encriptado)
        a: int = int(input("Ingresa el numero que consideres sea (a) el inverso del conjunto:"))
        print(f"\nCORRECTO:\nEl numero que ingresaste a: {a} corresponde al inverso del conjunto Z es:")
        print(self.criptografia.calcular_inverso(a))

    def desencriptar_mensaje(self):
        print("Descifrar mensaje:")
        print("El mensaje descifrado es:")
        palabra: str = self.criptografia.desencriptar_mensaje()
        print(palabra)










