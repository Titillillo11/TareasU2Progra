class Hospital:
    def __init__(self):
        self.medicos = []
        self.pacientes = []

    def agregar_medico(self, medico):
        self.medicos.append(medico)

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def mostrar_medicos(self):
        print("Médicos registrados:")
        for medico in self.medicos:
            print(f"Nombre: {medico.nombre}, ID: {medico.id_medico}")

    def mostrar_pacientes_menores(self):
        print("Pacientes menores de edad:")
        for paciente in self.pacientes:
            if paciente.edad < 18:
                print(f"Nombre: {paciente.nombre}, ID: {paciente.id_paciente}, Edad: {paciente.edad}")

    def mostrar_pacientes_mayores(self):
        print("Pacientes mayores de edad:")
        for paciente in self.pacientes:
            if paciente.edad >= 18:
                print(f"Nombre: {paciente.nombre}, ID: {paciente.id_paciente}, Edad: {paciente.edad}")

    def eliminar_paciente(self, id_paciente):
        self.pacientes = [paciente for paciente in self.pacientes if paciente.id_paciente != id_paciente]

    def eliminar_medico(self, id_medico):
        self.medicos = [medico for medico in self.medicos if medico.id_medico != id_medico]
