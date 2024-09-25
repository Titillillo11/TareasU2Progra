class Materia:
    def __init__(self, numero_control: str, nombre: str, descripcion: str, semestre: int, creditos: int):
        self.numero_control = numero_control
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos

    def mostrar_info_materia(self):
        info_materia = (f"Número de control: {self.numero_control}, "
                        f"Nombre: {self.nombre}, "
                        f"Descripción: {self.descripcion}, "
                        f"Semestre: {self.semestre}, "
                        f"Créditos: {self.creditos}")
        return info_materia
