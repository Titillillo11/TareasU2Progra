from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def generar_numero_control(self):
        numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0, 1000)}"
        return numero_control

    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)

    def generar_numero_control_mtro(self, nombre: str, rfc: str, ano_nacimiento: int):
        dia_actual = datetime.now().day
        numero_random = randint(500, 5000)
        numero_control = (f"M-{ano_nacimiento}-{dia_actual}-{numero_random}-{nombre[:2].upper()}{rfc[-2:].upper()}{len(self.lista_maestros) + 1}")
        return numero_control
