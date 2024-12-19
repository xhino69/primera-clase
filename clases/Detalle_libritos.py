from clases.Libritos import Libro
from clases.Edit import Editorial
class DetalleLibro(Libro, Editorial):
    def __init__(self, id_detalle_libro, isbn, id_editorial, numero_pagi, estado, n_copias, edicion):
        super.__init__(isbn)
        super.__init__(id_editorial)
        self.estado = estado
        self.n_copias = n_copias
        self.edicion = edicion
        self.numero_pagi = numero_pagi
        self.id_detalle_libro = id_detalle_libro