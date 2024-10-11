from datetime import datetime
from typing import List
from utils.roles import Rol

class Personal:

    nombre: str
    apellidos: str
    fecha_nacimiento: datetime
    fecha_ingreso_trabajar: datetime
    rfc: str
    curp: str
    salario: float
    horario: str
    rol: Rol

    def __init__(self, nombre: str, 
                 apellidos: str, 
                 fecha_nacimiento: datetime, 
                 fecha_ingreso_trabajar: datetime,
                 rfc: str,
                 curp: str,
                 salario: float,
                 horario: str,
                 rol: Rol):
        
        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_ingreso_trabajar = fecha_ingreso_trabajar
        self.rfc = rfc
        self.curp = curp
        self.salario = salario
        self.horario = horario
        self.rol = rol

