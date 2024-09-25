class Maestro:
    numero_control: str
    nombre: str
    apellido: str
    rfc: str
    sueldo: float

    def __init__(self, numero_control: str, nombre: str, apellido: str, rfc: str, sueldo: float):
        self.numero_control = numero_control
        self.nombre = nombre
        self.apellido = apellido
        self.rfc = rfc
        self.sueldo = sueldo

    def mostrar_info_maestro(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        info_maestro = f"\n Numero de control: {self.numero_control}, Nombre completo: {nombre_completo}, RFC: {self.rfc}, Sueldo: {self.sueldo}"
        return info_maestro