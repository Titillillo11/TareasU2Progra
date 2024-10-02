from datetime import datetime
from carrera.carrera import Carrera
from escuela.escuela import Escuela
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from semestre.semestre import Semestre


escuela = Escuela()

while True:
    print("\n*------------MINDBOX------------*\n")

    print("1. Mostrar estudiantes") 
    print("2. Mostrar maestros") 
    print("3. Mostrar materias") 
    print("4. Mostrar grupos") 
    print("5. Mostrar carreras") 
    print("6. Mostrar semestres") 
    
    print("\n*------------------------*\n")
    print("7. Registrar estudiante") 
    print("8. Registrar maestro") 
    print("9. Registrar materia") 
    print("10. Registrar grupo") 
    print("11. Registrar horario") 
    print("12. Registrar carrera") 
    print("13. Registrar semestre") 

    print("\n*------------------------*\n")
    print("14. Eliminar estudiante") 
    print("15. Eliminar maestro") 
    print("16. Eliminar materia") 
    print() 
    print("17. Salir")  
    print("\n*------------------------*\n")

    opcion = input("Ingresa una opción para continuar: ")

    if opcion == "1":
        escuela.listar_estudiantes()
        

    elif opcion == "2":
        escuela.listar_maestros() 


    elif opcion == "3":
        escuela.listar_materias()  


    elif opcion == "4":
        escuela.listar_grupos()  


    elif opcion == "5":
        escuela.listar_carreras() 


    elif opcion == "6":
        escuela.listar_semestres()  


    elif opcion == "7":
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


    elif opcion == "8":
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


    elif opcion == "9":
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


    elif opcion == "10":
        print("\nSeleccionaste la opción para registrar un nuevo grupo")
        tipo = input("Ingresa el tipo de grupo A/B: ")
        id_semestre = input("Ingresa el ID del semestre al que pertenece el grupo: ")

        grupo = Grupo(tipo=tipo, id_semestre=id_semestre)
        escuela.registrar_grupo(grupo)

    elif opcion == "11":
        pass  


    elif opcion == "12":
        nombre_carrera = input("Ingresa el nombre de la carrera: ")
        matricula = input("Ingresa la matrícula de la carrera: ")
        numero_semestres = int(input("Ingresa el número de semestres de la carrera: "))
        nueva_carrera = Carrera(matricula, nombre_carrera, numero_semestres)
        escuela.registrar_carrera(nueva_carrera)
        print(f"Carrera {nombre_carrera} registrada correctamente.")


    elif opcion == "13":
        print("\nSeleccionaste la opción para registrar un semestre")
        numero = input("Ingresa el número del semestre: ")
        id_carrera = input("Ingresa el ID de la carrera: ") 
        
        semestre = Semestre(numero=numero, id_carrera=id_carrera)
        escuela.registrar_semestre(semestre=semestre)


    elif opcion == "14":
        print("\nSeleccionaste la opción para eliminar un estudiante.")
        numero_control = input("Ingresa el número de control del estudiante: ")
        escuela.eliminar_estudiante(numero_control=numero_control)


    elif opcion == "15":
        num_control = input("Ingresa el número de control del maestro a eliminar: ")
        escuela.eliminar_maestro(num_control)


    elif opcion == "16":
        num_control = input("Ingresa el número de control de la materia a eliminar: ")
        escuela.eliminar_materia(num_control)


    elif opcion == "17":
        print("Hasta luego.")
        break
