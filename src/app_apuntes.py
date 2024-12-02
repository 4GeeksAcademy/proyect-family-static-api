class Coche ():
    def __init__(self,modelo,color):
        self.modelo = modelo
        self.color = color
    
    def __repr__(self):
        return f'este coche {self.modelo} y tiene {self.color}'


coche_uno = Coche (modelo="seat", color ="amarillo")
coche_dos = Coche (color="audi", modelo ="negro")


print(coche_uno)
print(coche_dos)