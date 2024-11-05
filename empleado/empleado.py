from persona.persona import Persona
from datetime import datetime

class Empleado(Persona):
    rfc: str
    sueldo: float
    anios_antiguedad: int
    horario: str

    def __init__(self, numero_control: str, nombre: str, apellido: str, rfc: str, sueldo: float, contrasenia: str, anios_antiguedad: int, horario: str, fecha_nacimiento: datetime):
        super().__init__(
            numero_control=numero_control,
            nombre=nombre,
            apellido=apellido,
            contrasenia=contrasenia,
            rol=None,
            curp="",
            fecha_nacimiento=fecha_nacimiento
        )
        self.rfc = rfc
        self.sueldo = sueldo
        self.anios_antiguedad = anios_antiguedad
        self.horario = horario


