class Persona:
    def __init__(self, nombre, apellido):
        self._nombre = nombre
        self._apellido = apellido
    
    def avanzar (self):
        print('Hola soy {} {} y ando caminando porque no estoy en clases'.format (self._nombre, self._apellido))



class Ciclista(Persona):
    def __init__(self, nombre,apellido):
        super().__init__(nombre, apellido)
    
    def avanzar(self):
        print('Hola, soy {} {} y ando moviendome en mi bicicleta'.format(self._nombre, self._apellido))

if __name__== "__main__":
    persona = Persona('Fabian', 'Ochoa')
    persona.avanzar() 
    ciclista = Ciclista('Roberto', 'Goyes')
    ciclista.avanzar()