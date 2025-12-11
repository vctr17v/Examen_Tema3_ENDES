from piso import Piso
from casa_unifamiliar import CasaUnifamiliar
from habitacion import Habitacion
from inquilino import Inquilino
from comunidad_vecinos import ComunidadDeVecinos

# crear viviendas
piso1 = Piso("Calle Mayor", "15", "Madrid", 85, 950, "3ºB", True, True)
piso1.añadir_habitacion(Habitacion("Dormitorio", 15, True))
piso1.añadir_habitacion(Habitacion("Salon", 25, True))
piso1.añadir_habitacion(Habitacion("Cocina", 12, True))
piso1.añadir_habitacion(Habitacion("Baño", 6, False))

piso2 = Piso("Calle Mayor", "15", "Madrid", 70, 850, "1ºA", False, True)
piso2.añadir_habitacion(Habitacion("Dormitorio", 12, True))
piso2.añadir_habitacion(Habitacion("Salon", 30, True))
piso2.añadir_habitacion(Habitacion("Baño", 5, False))

casa1 = CasaUnifamiliar("Avenida del Parque", "8", "Madrid", 150, 1500, True, "aislada", True)
casa1.añadir_habitacion(Habitacion("Dormitorio 1", 20, True))
casa1.añadir_habitacion(Habitacion("Dormitorio 2", 15, True))
casa1.añadir_habitacion(Habitacion("Salon", 35, True))
casa1.añadir_habitacion(Habitacion("Cocina", 18, True))
casa1.añadir_habitacion(Habitacion("Baño", 8, True))

# inquilinos
inquilino1 = Inquilino("Ana García", "12345678A", "666111222")
inquilino2 = Inquilino("Carlos López", "87654321B", "666333444")

# comunidad
comunidad = ComunidadDeVecinos("Comunidad Calle Mayor", "Calle Mayor 15, Madrid", 15000)
comunidad.añadir_vivienda(piso1)
comunidad.añadir_vivienda(piso2)

print("Estado inicial:")
print(comunidad)
print(piso1)
print(piso2)
print(casa1)
print(inquilino1)
print(inquilino2)

print("\nModificaciones:")
inquilino1.mudarse_a(piso1)
inquilino2.mudarse_a(casa1)
piso1.añadir_habitacion(Habitacion("Terraza", 8, True))
comunidad.retirar_vivienda(piso2)

print("\nEstado final:")
print(comunidad)
print(piso1)
print(casa1)
print(inquilino1)
print(inquilino2)
