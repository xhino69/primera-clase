from datetime import datetime

class Autor():
    def __init__(self, id_autor, nombre_autor, fecha_nac, fecha_def, nacionalidad):
        self.id_autor = id_autor
        self.nombre_autor = nombre_autor
        self.fecha_nac = fecha_nac
        self.fecha_def = fecha_def
        self.nacionalidad = nacionalidad
        
    def manejo_fechas(fecha):
        fecha_dt = datetime.strptime(fecha, '%d/%m/%Y')
        fecha_str = fecha_dt.strftime('%Y-%m-%d')
        return fecha_str