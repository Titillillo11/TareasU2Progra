from datetime import datetime
from typing import List

class Animal:

    tipo_animal: str
    fecha_nacimiento: datetime
    fecha_llegada: datetime
    peso: float 
    enfermedades: str
    frecuencia_alimentacion: str
    tipo_alimentacion: str
    vacunado: bool

    def __init__(self, tipo_animal: str, 
                 fecha_nacimiento: datetime, 
                 fecha_llegada: datetime, 
                 peso:float, 
                 enfermedades: List[str],
                 frecuencia_alimentacion: str, 
                 tipo_alimentacion: str, 
                 vacunado:bool):
        
        
        self.tipo_animal = tipo_animal
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_llegada = fecha_llegada
        self.peso = peso
        self.enfermedades = enfermedades  
        self.frecuencia_alimentacion = frecuencia_alimentacion
        self.tipo_alimentacion = tipo_alimentacion
        self.vacunado = vacunado  

