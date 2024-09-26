class Materia:
    def __init__(self, numero_control: str, nombre: str, descripcion: str, semestre: int, creditos: int):
        self.numero_control = numero_control
        self.nombre = nombre
        self.descripcion = descripcion
        self.semestre = semestre
        self.creditos = creditos

    def mostrar_info_materia(self):
        return (f"Número de control: {self.numero_control}\n"
                f"Nombre: {self.nombre}\n"
                f"Descripción: {self.descripcion}\n"
                f"Semestre: {self.semestre}\n"
                f"Créditos: {self.creditos}")
