from typing import List
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from grupos.grupo import Grupo
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from random import randint
from datetime import datetime

class Escuela:
    def __init__(self):
        self.lista_estudiantes: List[Estudiante] = []
        self.lista_maestros: List[Maestro] = []
        self.lista_grupos: List[Grupo] = []
        self.lista_materias: List[Materia] = []
        self.lista_carreras: List[Carrera] = []
        self.lista_semestres: List[Semestre] = []


    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)

    def generar_numero_control(self):
        numero_control = f"l{datetime.now().year}{datetime.now().month}{len(self.lista_estudiantes) + 1}{randint(0, 1000)}"
        return numero_control
    
    def listar_estudiantes(self):
        print("** ESTUDIANTES **")
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_info_estudiante())
        return  

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
        if not self.lista_maestros:
            print("No hay maestros registrados.")
        else:
            print("** MAESTROS **")
            for maestro in self.lista_maestros:
                print(maestro.mostrar_info_maestro())


    def eliminar_maestro(self, numero_control: str):
        for maestro in self.lista_maestros:
            if maestro.numero_control == numero_control:
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
        if not self.lista_materias:
            print("No hay materias registradas.")
        else:
            print("** MATERIAS **")
            for materia in self.lista_materias:
                print(materia.mostrar_info_materia())


    def eliminar_materia(self, numero_control_materia: str):
        for materia in self.lista_materias:
            if materia.numero_control == numero_control_materia:
                self.lista_materias.remove(materia)
                print("MATERIA ELIMINADA.")
                return
        print(f"No se encontró la materia con el número de control: {numero_control_materia}")


    def registrar_carrera(self, carrera: Carrera):
        self.lista_carreras.append(carrera)


    def registrar_semestre(self, semestre: Semestre):
        id_carrera = semestre.id

        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break

        self.lista_semestres.append(semestre)


    def registrar_grupo(self, grupo: Grupo):
        id_semestre = grupo.id_semestre

        for semestre in self.lista_semestres:
            if id_semestre == semestre.id:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break

        self.lista_grupos.append(grupo)


    def listar_carreras(self):
            if not self.lista_carreras:
                print("No hay carreras registradas.")
            else:
                print("\n** CARRERAS **")
                for carrera in self.lista_carreras:
                    print(f"Matrícula: {carrera.matricula}, Nombre: {carrera.nombre}, Número de Semestres: {carrera.numero_semestres}")

    def listar_semestres(self):
            if not self.lista_semestres:
                print("No hay semestres registrados.")
            else:
                print("\n** SEMESTRES **")
                for semestre in self.lista_semestres:
                    print(f"ID: {semestre.id}, Número: {semestre.numero}, ID Carrera: {semestre.id_carrera}")

    def listar_grupos(self):
            if not self.lista_grupos:
                print("No hay grupos registrados.")
            else:
                print("\n** GRUPOS **")
                for grupo in self.lista_grupos:
                    print(f"ID del Grupo: {grupo.id_grupo}, Tipo: {grupo.tipo}, ID del Semestre: {grupo.id_semestre}")


