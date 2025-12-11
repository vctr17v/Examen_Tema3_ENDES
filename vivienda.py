class Vivienda:
    def __init__(self, calle, numero, ciudad, superficie, precio_alquiler):
        self.calle = calle
        self.numero = numero
        self.ciudad = ciudad
        self.superficie = superficie
        self.precio_alquiler = precio_alquiler
        self.estado = "disponible"
        self.inquilino_actual = None
        self.habitaciones = []
    
    def asignar_inquilino(self, inquilino):
        if self.estado == "disponible":
            self.inquilino_actual = inquilino
            self.estado = "ocupada"
            return True
        return False
    
    def liberar_inquilino(self):
        self.inquilino_actual = None
        self.estado = "disponible"
    
    def añadir_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
    
    def get_direccion_completa(self):
        return f"{self.calle} {self.numero}, {self.ciudad}"
    
    def __str__(self):
        inquilino_info = f"Inquilino: {self.inquilino_actual.nombre}" if self.inquilino_actual else "Sin inquilino"
        habitaciones_str = ""
        if self.habitaciones:
            habitaciones_str = "\n  Habitaciones:"
            for hab in self.habitaciones:
                habitaciones_str += f"\n    - {hab}"
        return f"Vivienda en {self.get_direccion_completa()}\n  Superficie: {self.superficie} m²\n  Precio: {self.precio_alquiler}€/mes\n  Estado: {self.estado}\n  {inquilino_info}{habitaciones_str}"
