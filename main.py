from hospital import Hospital
from medico import Medico
from paciente import Paciente

def main():
    hospital = Hospital()

    medico1 = Medico("Dr. Pérez", "M001")
    medico2 = Medico("Dra. Gómez", "M002")
    hospital.agregar_medico(medico1)
    hospital.agregar_medico(medico2)

    paciente1 = Paciente("Ana", 15, "P001")
    paciente2 = Paciente("Luis", 22, "P002")
    paciente3 = Paciente("Juan", 17, "P003")
    hospital.agregar_paciente(paciente1)
    hospital.agregar_paciente(paciente2)
    hospital.agregar_paciente(paciente3)

    hospital.mostrar_medicos()
    print()
    hospital.mostrar_pacientes_menores()
    print()
    hospital.mostrar_pacientes_mayores()

    hospital.eliminar_paciente("P001")
    print("Después de eliminar paciente P001:")
    hospital.mostrar_pacientes_mayores()

    hospital.eliminar_medico("M001")
    print("Después de eliminar médico M001:")
    hospital.mostrar_medicos()

if __name__ == "__main__":
    main()
