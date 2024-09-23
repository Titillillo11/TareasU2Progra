"""
- Pacientes
- Médicos
- Consultas
- Medicamentos
"""

from paciente import Paciente
from medico import Medico
from hospital import Hospital

def mostrar_menu():
    print("----- Menú del Hospital -----")
    print("1. Mostrar pacientes menores de edad")
    print("2. Mostrar pacientes mayores de edad")
    print("3. Eliminar paciente")
    print("4. Eliminar médico")
    print("5. Mostrar todos los pacientes")
    print("6. Mostrar todos los médicos")
    print("0. Salir")

def main():
    hospital = Hospital()

    # Crear pacientes y médicos
    paciente = Paciente("Juan", 2004, 76, 1.78, "Avenida Madero")
    paciente_dos = Paciente("Jonathan", 2005, 70, 1.90, "Avenida Madero")
    medico = Medico("Alberto", 1900, "ALB4817BNDDDF", "Av. Periodismo")

    hospital.registrar_paciente(paciente=paciente)
    hospital.registrar_paciente(paciente=paciente_dos)
    hospital.registrar_medico(medico=medico)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            hospital.mostrar_pacientes_menores()
        elif opcion == "2":
            hospital.mostrar_pacientes_mayores()
        elif opcion == "3":
            id_paciente = input("Ingrese el ID del paciente a eliminar: ")
            hospital.eliminar_paciente(id_paciente)
            print("Paciente eliminado.")
        elif opcion == "4":
            id_medico = input("Ingrese el ID del médico a eliminar: ")
            hospital.eliminar_medico(id_medico)
            print("Médico eliminado.")
        elif opcion == "5":
            hospital.mostrar_pacientes()
        elif opcion == "6":
            hospital.mostrar_medicos()
        elif opcion == "0":
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
