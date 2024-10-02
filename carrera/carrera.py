from typing import List
from semestre.semestre import Semestre
from random import randint

class Carrera:
    def __init__(self, nombre: str):
        self.matricula = self.generar_id(nombre)
        self.nombre = nombre
        self.numero_semestres: int = 0  
        self.semestres: List[Semestre] = [] 

    def generar_id(self, nombre: str) -> str:
        return f"{nombre}-{randint(0, 10000)}-{randint(0, 10000)}"
    
    def registrar_semestre(self, semestre: Semestre):
        self.numero_semestres += 1
        self.semestres.append(semestre)
