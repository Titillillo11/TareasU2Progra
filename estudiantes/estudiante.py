from datetime import datetime

class Estudiante:
    num_control: str
    nombre: str
    apellido: str
    curp: str
    fecha_nacimiento: datetime

    def __init__(self, numero_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime):
        self.num_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_info_estudiante(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info = f"\nNúmero de control: {self.num_control}, Nombre completo: {nombre_completo}, CURP: {self.curp}, Fecha de nacimiento: {self.fecha_nacimiento.strftime('%d/%m/%Y')}"
        return info
