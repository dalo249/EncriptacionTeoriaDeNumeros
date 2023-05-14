import random


class Criptografia:

    def __init__(self):

        self.alfabeto: list[str] = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                                    "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                                    "v", "w", "x", "y", "z", "á", "é", "í", "ó", "ú", "A",
                                    "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                                    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W",
                                    "X", "Y", "Z", "Á", "É", "Í", "Ó", "Ú", "1", "2", "3",
                                    "4", "5", "6", "7", "8", "9", "0", "+", "-", "*", "/",
                                    "^", "%", "#", "$", "@", " ", ",", ";", ".", ":", "¿",
                                    "?", "¡", "!", "(", ")", "[", "]", "{", "}", " \ ", "=",
                                    "¬", "ñ", "Ñ", "ü", "Ü"]

        self.hexadecimales: list[str] = ["0061", "0062", "0063", "0064", "0065", "0066", "0067", "0068", "0069",
                                         "006A", "006B", "006C", "006D", "006E", "006F", "0070", "0071", "0072",
                                         "0073", "0074", "0075", "0076", "0077", "0078", "0079", "007A", "00E1",
                                         "00E9", "00ED", "00F3", "00FA", "0041", "0042", "0043", "0044", "0045",
                                         "0046", "0047", "0048", "0049", "004A", "004B", "005C", "004D", "004E",
                                         "004F", "0050", "0051", "0052", "0053", "0054", "0055", "0056", "0057",
                                         "0058", "0059", "005A", "00C1", "00C9", "00CD", "00D3", "00DA", "0031",
                                         "0032", "0033", "0034", "0035", "0036", "0037", "0038", "0039", "001A",
                                         "002A", "002B", "002C", "002D", "002E", "002F", "0023", "0024", "0025",
                                         "0040", "003A", "003B", "003C", "003D", "003E", "003F", "00A1", "0021",
                                         "005F", "0028", "0029", "005B", "005D", "007B", "007D", "005E", "00AC"
                                         "00F1", "00D1", "00FC", "00DC", "0020"]
        self.n: int = len(self.alfabeto)
        self.a: int = 0
        self.b: int = 0
        self.encriptado: list[str] = list()
        self.a_ive = 0

    def aleatorio(self) -> int:
        numero: int = random.randint(9999999999, 99999999999999)
        return numero

    def generar_cociente_a(self):
        a: int = self.aleatorio()
        while self.calcular_mcd(a) is False:
            a: int = self.aleatorio()
            self.calcular_mcd(a)
        self.a = a

    def calcular_mcd(self, a: int) -> bool:
        x: int = self.n
        y: int = a % self.n
        while y != 0:
            mcd: int = y
            y = x % y
            x = mcd
        if x == 1:
            return True
        else:
            return False

    def generar_independiente_b(self):
        b: int = self.aleatorio()
        self.b: int = b

    def calcular_ecuacion(self, indice: int) -> int:

        y: int
        y = (((self.a % self.n)*indice) + (self.b % self.n)) % self.n
        return y

    def mostrar_ecuacion(self) -> str:
        ecuacion: str = f"f(x) = {(self.a % self.n)}*x + {(self.b % self.n)} (MOD {self.n} )"
        return ecuacion

    def calcular_encriptacion(self, mensaje: str) -> list[str]:
        encriptado: list[str] = list()
        for x in mensaje:
            indice: int = self.alfabeto.index(x)
            y: int = self.calcular_ecuacion(indice)
            encriptado.append(self.hexadecimales[y])
        self.encriptado: list[str] = encriptado
        return encriptado

    def orden_mensaje_encriptado(self, encriptado: list[str], orden: list[int]) -> str:
        encriptado: str = "".join(encriptado)
        mensaje: list[str] = [str(self.a), str(self.b), encriptado]
        mensaje_encriptado: str = mensaje[orden[0]]+"&"+mensaje[orden[1]]+"&"+mensaje[orden[2]]
        return mensaje_encriptado

    def mostrar_mensaje_encriptado(self, mensaje_encriptado: str) -> str:
        return f" El mensaje final encriptado es: \n {mensaje_encriptado}"

    def generar_ecuacion(self) -> str:
        self.generar_cociente_a()
        self.generar_independiente_b()
        return self.mostrar_ecuacion()

    def encriptar_mensaje(self, mensaje: str, orden: list[int]) -> str:
        encriptado: list[str] = self.calcular_encriptacion(mensaje)
        mensaje_encriptado: str = self.orden_mensaje_encriptado(encriptado, orden)
        return self.mostrar_mensaje_encriptado(mensaje_encriptado)

    def calcular_inverso(self, a: int) -> str:
        if self.calcular_mcd(a):
            a_ive = pow(a, -1, self.n)
            self.a_ive = a_ive
            return a_ive

    def calcular_division(self, indice: int):
        x: int
        x = (((indice - (self.b % self.n)) * (self.a_ive % self.n)) % self.n)
        return x

    def calcular_desencriptacion(self) -> list[str]:
        letras: list[str] = list()
        for x in self.encriptado:
            indice: int = self.hexadecimales.index(x)
            y: int = self.calcular_division(indice)
            letra: str = self.alfabeto[y]
            letras.append(letra)
        return letras

    def mostrar_palabra(self, letras: list[str]) -> str:
        palabra: str = "".join(letras)
        return palabra

    def desencriptar_mensaje(self) -> str:
        letras: list[str] = self.calcular_desencriptacion()
        return self.mostrar_palabra(letras)


















