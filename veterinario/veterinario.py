from empleado.empleado import Empleado  
from persona.utils.roles import Rol  
#from datetime import datetime

class Veterinario(Empleado):
    def __init__(self, numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento, especialidad):
        super().__init__(numero_control, nombre, apellido, rfc, sueldo, contrasenia, anios_antiguedad, horario, fecha_nacimiento)
        self.especialidad = especialidad

        self.rol = Rol.VETERINARIO  
