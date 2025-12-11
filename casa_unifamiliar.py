from vivienda import Vivienda

class CasaUnifamiliar(Vivienda):
    def __init__(self, calle, numero, ciudad, superficie, precio_alquiler, tiene_patio_jardin=True, tipo="aislada", tiene_aparcamiento=True):
        super().__init__(calle, numero, ciudad, superficie, precio_alquiler)
        self.tiene_patio_jardin = tiene_patio_jardin
        self.tipo = tipo
        self.tiene_aparcamiento = tiene_aparcamiento
    
    def __str__(self):
        inquilino = self.inquilino_actual.nombre if self.inquilino_actual else "disponible"
        return f"Casa {self.tipo} - {self.get_direccion_completa()}, {self.superficie}m2, {self.precio_alquiler}€, {inquilino}"
