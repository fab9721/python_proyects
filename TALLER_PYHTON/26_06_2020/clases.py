class Rectangulo :
    def __init__(self, base, altura):
        self._base = base
        self._altura = altura
    
    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, valor):
        self._base = valor
    
    @property
    def altura(self):
        return self._altura
    
    @altura.setter
    def altura(self, valor):
        self._altura = valor

    def calcular_area(self):
        return self._base * self._altura

    
class Cuadrado(Rectangulo):
        def __init__(self, lado):
            super().__init__(lado, lado)
    
    
    
if __name__ == "__main__":
        rectangulo = Rectangulo(10,20)
        print('Rectangulo -> Base:{} Altura:{} Area: {}'.format(rectangulo._base, rectangulo._altura, rectangulo.calcular_area()))

        cuadrado = Cuadrado(20)
        print('Cuadrado -> Lado:{}  Area: {}'.format(cuadrado._base, cuadrado.calcular_area()))
