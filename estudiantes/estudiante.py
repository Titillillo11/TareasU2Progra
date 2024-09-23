import datetime

class Estudiante:
    num_control: str
    nombre: str
    apellido: str
    curp: str
    fecha_nacimiento: datetime

    def __init__(self, numero_control: str, nombre: str, apellido: str, curp:  str, fecha_nacimiento: datetime):
        self.num_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento

