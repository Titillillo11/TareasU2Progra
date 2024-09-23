
class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def mostrar_informacion(self):
        print(f"Coche: {self.marca} {self.modelo}, Año: {self.año}")

    def calcular_edad_del_coche(self, año_actual):
        return año_actual - self.año
