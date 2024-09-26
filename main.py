from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
from materias.materia import Materia 
from datetime import datetime
from random import randint

escuela = Escuela()

while True:
    print("\n**MINDBOX**\n")

    print("1. Registrar estudiante")
    print("2. Registrar maestro")
    print("3. Registrar materia")
    print("4. Registrar grupo")
    print("5. Registrar horario")
    print("6. Mostrar estudiantes")
    print("7. Mostrar maestros")
    print("8. Mostrar materias")
    print("9. Mostrar grupos")
    print("10. Eliminar estudiante")
    print("11. Eliminar maestro")
    print("12. Eliminar materia")
    print("13. Salir")

    opcion = input("Ingresa una opción para continuar: ")

    if opcion == "1":
        print("\nSeleccionaste la opción para registrar un estudiante")
        numero_control = escuela.generar_numero_control()

        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        curp = input("Ingrese la CURP del estudiante: ")
        ano = int(input("Ingrese el año de nacimiento del estudiante: "))
        mes = int(input("Ingrese el mes de nacimiento del estudiante: "))
        dia = int(input("Ingrese el día de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)

        estudiante = Estudiante(numero_control=numero_control, nombre=nombre, apellido=apellido, curp=curp, fecha_nacimiento=fecha_nacimiento)
        escuela.registrar_estudiante(estudiante)
        print(f"Estudiante {nombre} registrado exitosamente.")

    elif opcion == "2":
        print("\nSeleccionaste la opción para registrar un maestro")
        nombre = input("Ingresa el nombre del maestro: ")
        apellido = input("Ingresa el apellido del maestro: ")
        rfc = input("Ingresa el RFC del maestro: ")
        ano_nacimiento = int(input("Ingresa el año de nacimiento del maestro: "))
        sueldo = float(input("Ingresa el sueldo del maestro: "))

        numero_control = escuela.generar_numero_control_mtro(nombre, rfc, ano_nacimiento)
        print(f"Número de control generado: {numero_control}")

        maestro = Maestro(numero_control, nombre, apellido, rfc, sueldo)
        escuela.registrar_maestro(maestro)
        print(f"Maestro {nombre} registrado exitosamente.")

    elif opcion == "3":
        print("\nSeleccionaste la opción para registrar una materia")
        nombre = input("Ingrese el nombre de la materia: ")
        descripcion = input("Ingrese la descripción de la materia: ")
        semestre = int(input("Ingrese el semestre de la materia: "))
        creditos = int(input("Ingrese la cantidad de créditos de la materia: "))

        numero_control = escuela.generar_numero_control_materia(nombre, semestre, creditos)
        print(f"Número de control generado: {numero_control}")

        materia = Materia(numero_control, nombre, descripcion, semestre, creditos)
        escuela.registrar_materia(materia)
        print(f"Materia {nombre} registrada exitosamente.")

    elif opcion == "6":
        escuela.listar_estudiantes()

    elif opcion == "7":
        escuela.Listar_maestros()

    elif opcion == "8":
        escuela.Listar_materias()

    elif opcion == "10":
        print("\nSeleccionaste la opcion para eliminar un estudiante. ")
        numero_control = input("Ingresa el numero de control del estudiante: ")
        escuela.eliminar_estudiante(numero_control=numero_control)

    elif opcion == "11":
        num_control = input("Ingresa el número de control del maestro a eliminar: ")
        escuela.eliminar_maestro(num_control) 

    elif opcion == "12":
        num_control = input("Ingresa el número de control de la materia a eliminar: ")
        escuela.eliminar_materia(num_control) 

    elif opcion == "13":
        print("Hasta luego.")
        break
