from datetime import datetime

class Maestro:
    def __init__(self, numero_control: str, nombre: str, apellido: str, rfc: str, sueldo: float):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo

