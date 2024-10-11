from datetime import datetime

class Visitante:

    nombre_visitante: str
    fecha_nacimiento: datetime
    apellidos: str
    curp: str
    fecha_registro: datetime
    numero_visitas: int


    def __init__(self, nombre_visitante: str, 
                 fecha_nacimiento: datetime,
                 apellidos: str,
                 curp: str,
                 fecha_registro: datetime,
                 numero_visitas: int = 0): 
        
        
        self.nombre_visitante=nombre_visitante
        self.fecha_nacimiento=fecha_nacimiento
        self.apellidos=apellidos
        self.curp=curp
        self.fecha_registro=fecha_registro
        self.numero_visitas=numero_visitas
