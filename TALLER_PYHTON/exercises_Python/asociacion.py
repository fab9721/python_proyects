class Automovil:
    def __init__(self, modelo,marca,color,estado, motor):
        self._modelo= modelo
        self._marca = marca
        self._color = color
        self._estado = 'en reposo'
        self._motor = motor(cilindro = 5)

    def acelerar(self, tipo = 'despacio'):
        if tipo == 'rapido':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        self._estado = 'en movimiento'
        

class Motor:
    def __init__(self, cilindros, tipo ='gasolina'):
        self._cilindros = cilindros
        self._tipo = tipo
        self._temperatura = 0
    
    def inyecta_gasolina(self,cantidad ):
        self._cantidad = 20
        print('La cantidad de Gasolina es {}'.format(self._cantidad))
        pass

if __name__== "__main__":
    motor = Motor('Roberto', 'Renault')
    motor.inyecta_gasolina(cantidad=20)



