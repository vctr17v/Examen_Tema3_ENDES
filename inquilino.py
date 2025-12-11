class Inquilino:
    def __init__(self, nombre, dni, telefono):
        self.nombre = nombre
        self.dni = dni
        self.telefono = telefono
        self.vivienda_actual = None
    
    def mudarse_a(self, vivienda):
        if self.vivienda_actual:
            self.vivienda_actual.liberar_inquilino()
        if vivienda.asignar_inquilino(self):
            self.vivienda_actual = vivienda
            return True
        return False
    
    def dejar_vivienda(self):
        if self.vivienda_actual:
            self.vivienda_actual.liberar_inquilino()
            self.vivienda_actual = None
    
    def __str__(self):
        vivienda = self.vivienda_actual.get_direccion_completa() if self.vivienda_actual else "sin vivienda"
        return f"Inquilino {self.nombre} ({self.dni}) - {vivienda}"
