class Avion:
    def __init__(self, modeloavion, asientos):
        self.modeloavion = modeloavion
        self.asientos = asientos

class Aviones:
    def __init__(self):
        self.aviones = []

    def aviones_disponibles(self, avion):
        self.aviones.append(avion)

disponibilidad_aviones = Aviones()

avion_17 = Avion("bartolome 14", 60)

disponibilidad_aviones.aviones_disponibles(avion_17)

print("Aviones disponibles:")
for avion in disponibilidad_aviones.aviones:
    print(f"Modelo: {avion.modeloavion}, Asientos: {avion.asientos}")