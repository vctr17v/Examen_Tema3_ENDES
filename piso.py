from vivienda import Vivienda

class Piso(Vivienda):
    def __init__(self, calle, numero, ciudad, superficie, precio_alquiler, numero_puerta, tiene_garaje=False, tiene_trastero=False):
        super().__init__(calle, numero, ciudad, superficie, precio_alquiler)
        self.numero_puerta = numero_puerta
        self.tiene_garaje = tiene_garaje
        self.tiene_trastero = tiene_trastero
    
    def __str__(self):
        extras = []
        if self.tiene_garaje:
            extras.append("garaje")
        if self.tiene_trastero:
            extras.append("trastero")
        extras_info = f" ({', '.join(extras)})" if extras else ""
        inquilino = self.inquilino_actual.nombre if self.inquilino_actual else "disponible"
        return f"Piso {self.numero_puerta} - {self.get_direccion_completa()}, {self.superficie}m2, {self.precio_alquiler}€{extras_info}, {inquilino}"
