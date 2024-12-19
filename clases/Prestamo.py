from datetime import datetime
from clases.Detalle_libritos import DetalleLibro
from clases.Usuario import Usuario

class Prestamo(DetalleLibro, Usuario):
    def __init__(self, id_prestamo, isbn, id_usuario, fecha_prestamos, fecha_devolucion, fecha_efectiva_dev):
        super.__init__(isbn)
        super.__init__(id_usuario)
        self.fecha_prestamo = fecha_prestamos
        self.fecha_devolucion = fecha_devolucion
        self.fecha_devuelto = fecha_efectiva_dev
        self.id_prestamo = id_prestamo

    def calcular_fechas(self):
        if(self.n_copias > 0):
            self.fecha_prestamo = datetime.datetime.now()
            dias_de_prestamo = 7
            self.fecha_devolucion = self.fecha_prestamo() + dias_de_prestamo