class Retangulo(object):
    def __init__(self, largura, altura, ponto_inicial):
        self.__largura = largura
        self.__altura = altura
        self.__ponto_inicial = ponto_inicial

    def calculaCentro(self):
        x = self.__ponto_inicial.get_x() + (self.__largura / 2)
        y = self.__ponto_inicial.get_y() + (self.__altura / 2)
        return "As Coordenadas do centro são(%.1f, %.1f)" %(x, y)

class Ponto:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

def main():

    retangulo = None
    entrada = input().split()
    retangulo = Retangulo(int(entrada[0]), int(entrada[1]), Ponto(int(entrada[2]),int(entrada[3])))
    print(retangulo.calculaCentro())
main()
    
