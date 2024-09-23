from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from maestros.maestro import Maestro
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
    print("6. Salir")

    opcion = input("Ingresa una opción para continuar: ")

    if opcion == "1":
        print("\nSeleccionaste la opción para registrar un estudiante")
        numero_control = escuela.generar_numero_control()
        print(f"Número de control generado: {numero_control}")
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        curp = input("Ingrese la CURP del estudiante: ")
        ano = int(input("Ingrese el año de nacimiento del estudiante: "))
        mes = int(input("Ingrese el mes de nacimiento del estudiante: "))
        dia = int(input("Ingrese el día de nacimiento del estudiante: "))
        fecha_nacimiento = datetime(ano, mes, dia)

        estudiante = Estudiante(numero_control, nombre, apellido, curp, fecha_nacimiento)
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
        pass  

    elif opcion == "4":
        pass  

    elif opcion == "5":
        pass 

    elif opcion == "6":
        print("Hasta luego.")
        break
