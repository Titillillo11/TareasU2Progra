from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from grupos.grupo import Grupo
from datetime import datetime


class Menu:
    escuela: Escuela = Escuela()

    def mostrar_menu(self):
        while True:
            print("\n*------------MINDBOX------------*\n")
            print("1. Mostrar estudiantes")
            print("2. Mostrar maestros")
            print("3. Mostrar materias")
            print("4. Mostrar grupos")
            print("5. Mostrar carreras")
            print("6. Mostrar semestres")

            print("\n------------------------\n")
            print("7. Registrar estudiante")
            print("8. Registrar maestro")
            print("9. Registrar materia")
            print("10. Registrar grupo")
            print("11. Registrar horario")
            print("12. Registrar carrera")
            print("13. Registrar semestre")

            print("\n------------------------\n")
            print("14. Eliminar estudiante")
            print("15. Eliminar maestro")
            print("16. Eliminar materia")
            print()
            print("17. Salir")
            print("\n------------------------\n")

            opcion = input("Ingresa una opción para continuar: ")

            if opcion == "1":
                self.escuela.listar_estudiantes()
            elif opcion == "2":
                self.escuela.listar_maestros()
            elif opcion == "3":
                self.escuela.listar_materias()
            elif opcion == "4":
                self.escuela.listar_grupos()
            elif opcion == "5":
                self.escuela.listar_carreras()
            elif opcion == "6":
                self.escuela.listar_semestres()
            elif opcion == "7":
                self.registrar_estudiante()
            elif opcion == "8":
                self.registrar_maestro()
            elif opcion == "9":
                self.registrar_materia()
            elif opcion == "10":
                self.registrar_grupo()
            elif opcion == "11":
                pass
            elif opcion == "12":
                self.registrar_carrera()
            elif opcion == "13":
                self.registrar_semestre()
            elif opcion == "14":
                self.eliminar_estudiante()
            elif opcion == "15":
                self.eliminar_maestro()
            elif opcion == "16":
                self.eliminar_materia()
            elif opcion == "17":
                print("Adiós =)")
                break
            else:
                print("Opción no válida. Intenta de nuevo.")


    def registrar_estudiante(self):
        print("\n\t---- Registrar estudiante ----")
        numero_control = self.escuela.generar_numeroControl_E()
        print("Número de control: ", numero_control)
        nombre = input("Ingresa el nombre del estudiante: ")
        apellido = input("Ingresa el apellido del estudiante: ")
        curp = input("Ingresa la CURP del estudiante: ")
        print("Ingresa su fecha de nacimiento: ")
        año = int(input("Año: "))
        mes = int(input("Mes: "))
        dia = int(input("Día: "))
        fecha_nacimiento = datetime(año, mes, dia)
        contraseña = input("Ingresa una contraseña: ")
        estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento, contraseña=contraseña)
        self.escuela.registrar_estudiante(estudiante=estudiante)

    def registrar_maestro(self):
        print("\n\t---- Registrar maestro ----")
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        ano_nacimiento = input("Ingresa su año de nacimiento: ")
        rfc = input("Ingresa el RFC del maestro: ")
        sueldo = float(input("Ingresa el sueldo por hora: "))
        numero_control = self.escuela.generar_numeroControl_M(ano_nacimiento, nombre, rfc)
        print("Número de control: ", numero_control)
        contraseña = input("Ingresa una contraseña: ")
        maestro = Maestro(nombre=nombre, apellido=apellido, ano_nacimiento=ano_nacimiento, rfc=rfc, sueldo=sueldo, numero_control=numero_control, contraseña=contraseña)
        self.escuela.registrar_maestro(maestro=maestro)

    def registrar_materia(self):
        print("\n\t---- Registrar materia ----")
        nombre = input("Ingresa el nombre de la materia: ")
        descripcion = input("Ingresa la descripción de la materia: ")
        creditos = int(input("Ingresa la cantidad de créditos de la materia: "))
        semestre = int(input("Ingresa el semestre al que pertenece la materia: "))
        id = self.escuela.generar_id_materia(nombre=nombre, semestre=semestre, creditos=creditos)
        print("ID: ", id)
        materia = Materia(nombre=nombre, descripcion=descripcion, creditos=creditos, semestre=semestre, id=id)
        self.escuela.registrar_materia(materia=materia)

    def registrar_grupo(self):
        print("\n\t---- Registrar grupo ----")
        tipo = input("Ingresa el tipo de grupo (A/B): ")
        id_semestre = input("Ingresa el ID del semestre al que pertenece el grupo: ")
        grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
        self.escuela.registrar_grupo(grupo=grupo)

    def registrar_carrera(self):
        print("\n\t---- Registrar carrera ----")
        nombre = input("Ingresa el nombre de la carrera: ")
        carrera = Carrera(nombre=nombre)
        self.escuela.registrar_carrera(carrera)

    def registrar_semestre(self):
        print("\n\t---- Registrar semestre ----")
        numero = input("Ingresa el número del semestre: ")
        id_carrera = input("Ingresa el ID de la carrera: ")
        semestre = Semestre(numero=numero, id_carrera=id_carrera)
        self.escuela.registrar_semestre(semestre=semestre)

    def eliminar_estudiante(self):
        print("\n\t---- Eliminar estudiante ----")
        numero_control = input("Ingresa el número de control del estudiante a eliminar: ")
        self.escuela.eliminar_estudiante(numero_control)

    def eliminar_maestro(self):
        print("\n\t---- Eliminar maestro ----")
        numero_control = input("Ingresa el número de control del maestro a eliminar: ")
        self.escuela.eliminar_maestro(numero_control)

    def eliminar_materia(self):
        print("\n\t---- Eliminar materia ----")
        id = input("Ingresa el ID de la materia a eliminar: ")
        self.escuela.eliminar_materia(id)
