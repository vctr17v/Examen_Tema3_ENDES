class Habitacion:
    def __init__(self, nombre, superficie, tiene_ventana=True):
        self.nombre = nombre
        self.superficie = superficie
        self.tiene_ventana = tiene_ventana
    
    def __str__(self):
        ventana = "con ventana" if self.tiene_ventana else "sin ventana"
        return f"{self.nombre}: {self.superficie} m² ({ventana})"
