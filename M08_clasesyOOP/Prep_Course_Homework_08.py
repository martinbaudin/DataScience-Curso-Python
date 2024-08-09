from dataclasses import dataclass as dc

@dc
class vehiculo:
    color: str
    cilindrada: int
    tipo: str
    
    velocidad = 0
    direccion_actual = 'Norte'
    
    def acelerar(self):
        if self.velocidad < 240 and self.velocidad >= 0:
            self.velocidad += 60
            print('Acelerando...')
        else:
            print('Velocidad Máxima...')
            
    def frenar(self):
        print('Frenando...')
        
    def doblar(self):
        if self.direccion_actual == 'Norte':
            self.direccion_actual = 'Oeste'
        elif self.direccion_actual == 'Oeste':
            self.direccion_actual = 'Sur'
        elif self.direccion_actual == 'Sur':
            self.direccion_actual = 'Este'
        else:
            self.direccion_actual = 'Norte'
        
    def estado(self):
        print(f'Velocidad: {self.velocidad} | Direccion: {self.direccion_actual}')
    
    def __str__(self):
        print(f'Color: {self.color} | Cilindrada: {self.cilindrada} | Tipo: {self.tipo}')

auto = vehiculo('Rojo', 150, 'Moto')
auto.__str__()    

# auto.acelerar()
# auto.acelerar()
# auto.acelerar()
# auto.acelerar()
# auto.acelerar()
# auto.acelerar()
# auto.frenar()
auto.doblar()
auto.doblar()
auto.doblar()
auto.estado()