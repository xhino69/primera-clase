from clases.Tipo_de_usuario import Tipo_Usuario
from rut_chile import rut_chile
class Usuario(Tipo_Usuario):
    def __init__(self, id_usuario, name_usuario, apellido, fecha_nacimiento, cel_usuario, rut_usuario, id_tipo_usuario):
        super.__init__(id_tipo_usuario)
        self.id_usuario = id_usuario
        self.nombre_usuario = name_usuario
        self.apellido = apellido 
        self.cel_usuario = cel_usuario
        self.rut_usuario = rut_usuario
        self.fecha_nacimiento = fecha_nacimiento
    
    def validar_rut(self):
        return rut_chile.is_valid_rut(self.rut_usuario)