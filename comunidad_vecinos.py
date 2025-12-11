class ComunidadDeVecinos:
    def __init__(self, nombre, direccion, presupuesto_anual):
        self.nombre = nombre
        self.direccion = direccion
        self.presupuesto_anual = presupuesto_anual
        self.viviendas = []
    
    def añadir_vivienda(self, vivienda):
        if vivienda not in self.viviendas:
            self.viviendas.append(vivienda)
            return True
        return False
    
    def retirar_vivienda(self, vivienda):
        if vivienda in self.viviendas:
            self.viviendas.remove(vivienda)
            return True
        return False
    
    def get_numero_viviendas(self):
        return len(self.viviendas)
    
    def __str__(self):
        return f"Comunidad {self.nombre} - {len(self.viviendas)} viviendas, presupuesto: {self.presupuesto_anual}€"
