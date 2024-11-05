from persona.persona import Persona
from datetime import datetime

class Visitante(Persona):
    numero_visitas = int
    fecha_registro = datetime
    edad = str

    def __init__(self, numero_control: str, nombre: str, apellido: str, contrasenia: str, fecha_nacimiento: datetime,
                 numero_visitas=numero_visitas, fecha_registro=fecha_registro, edad=edad):
        super().__init__(
            numero_control=numero_control,
            nombre=nombre,
            apellido=apellido,
            contrasenia=contrasenia,
            rol=None,
            curp="",
            fecha_nacimiento=fecha_nacimiento
        )
        self.numero_visitas = numero_visitas
        self.fecha_registro = fecha_registro
        self.edad = edad
