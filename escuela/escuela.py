from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from datetime import datetime
from random import randint

class Escuela:
    def __init__(self):
        self.lista_estudiantes: List[Estudiante] = [] 
        self.lista_maestros: List[Maestro] = []       
        self.lista_grupos: List[Grupo] = []           
        self.lista_materias: List[Materia] = []       

    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def generar_numero_control(self):
        numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0, 1000)}"
        return numero_control
    
    def Listar_estudiantes(self):
        print("** ESTUDIANTES **")
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())  # No pasar self aquí
        return  # Mueve el return fuera del for

    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.num_control == numero_control:
                self.lista_estudiantes.remove(estudiante)
                print("ESTUDIANTE ELIMINADO.")
                return
            
        print(f"No se encontró el estudiante con el número de control: {numero_control}")


    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)

    def generar_numero_control_mtro(self, nombre: str, rfc: str, ano_nacimiento: int):
        dia_actual = datetime.now().day
        numero_random = randint(500, 5000)
        numero_control = (f"M-{ano_nacimiento}-{dia_actual}-{numero_random}-{nombre[:2].upper()}{rfc[-2:].upper()}{len(self.lista_maestros) + 1}")
        return numero_control
    

    def Listar_maestros(self):
        print("** MAESTROS **")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_info_maestro())
        return

    def eliminar_maestro(self, numero_control: str):
        for maestro in self.lista_maestros:
            if maestro.num_control == numero_control:
                self.lista_maestros.remove(maestro)
                print("MAESTRO ELIMINADO.")
                return
        print(f"No se encontró el maestro con el número de control: {numero_control}")


    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)

    def generar_numero_control_materia(self, nombre: str, semestre: int, creditos: int):
        ultimos_dos_digitos_nombre = nombre[-2:].upper()
        numero_random = randint(1, 1000)
        numero_control_materia = f"MT{ultimos_dos_digitos_nombre}{semestre}{creditos}{numero_random}"
        return numero_control_materia
    
    def Listar_materias(self):
        print("** MATERIAS **")
        for materia in self.lista_materias:
            print(materia.mostrar_info_materia())
        return


    def eliminar_materia(self, numero_control_materia: str):
    for materia in self.lista_materias:
        if materia.num_control_materia == generar_numero_control_materia:
            self.lista_materias.remove(materia)
            print("MATERIA ELIMINADA.")
            return
    print(f"No se encontró la materia con el número de control: {generar_numero_control_materia}")


