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

    def aleatorio(self) -> int:

        numero: int
        numero = random.randint(9999999999, 99999999999999)
        return numero

    def generar_cociente_a(self):
        a: int = self.aleatorio()
        self.a = a

    def generar_independiente_b(self):
        b: int = self.aleatorio()
        self.b: int = b

    def calcular_ecuacion(self, indice: int) -> int:

        y: int
        y = (((self.a % self.n)*indice) + (self.b % self.n)) % self.n
        return y

    def generar_ecuacion(self,) -> str:

        self.generar_cociente_a()
        self.generar_independiente_b()
        ecuacion: str = f"f(x) = {(self.a % 104)}*x + {(self.b  % 104)} (MOD {self.n})"
        return ecuacion

    def encriptar_mensaje(self, mensaje: str) -> list[str]:
        self.generar_ecuacion()
        mensaje_encriptado: list[str] = list()
        for x in mensaje:
            indice: int = self.alfabeto.index(x)
            y: int = self.calcular_ecuacion(indice)
            mensaje.append(self.hexadecimales[y])
        return mensaje












c =Criptografia()
print(c.encriptar_mensaje("carro"))
print(30 % 104)
#f(x) = ((a*x + b)%self.n)"

