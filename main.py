from estudiante import Estudiante
from curso import Curso

def main():
    curso1 = Curso("Matemáticas", "MAT101", "Dr. Pérez")
    curso2 = Curso("Programación", "PROG202", "Ing. López")
    curso3 = Curso("Historia", "HIST303", "Prof. García")

    estudiante1 = Estudiante("Ana", 20, "E001")
    estudiante2 = Estudiante("Luis", 22, "E002")

    estudiante1.agregar_curso(curso1)
    estudiante1.agregar_curso(curso2)

    estudiante2.agregar_curso(curso2)
    estudiante2.agregar_curso(curso3)

    estudiante1.mostrar_informacion()
    print()
    estudiante2.mostrar_informacion()

if __name__ == "__main__":
    main()
