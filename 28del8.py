class Avion:
    def __init__(self, modeloavion, asientos):
        self.modeloavion = modeloavion
        self.asientos = asientos
    def __str__(self):
        return f"{self.modeloavion}"    
class vuelo:
     def __init__(self, nvuelo, origen, destino, fecha, hora, _avion ):
         self.nvuelo = nvuelo
         self.origen=origen
         self.destino= destino
         self.fecha= fecha
         self.hora=hora
         self._avion=_avion
class Vuelos:
    def __init__(self):
        self.Vuelos = []

    def Vuelos_disponibles(self, avuelo):
        self.Vuelos.append(avuelo)
    def mostrar_vuelos(_vuelo):
        print("Vuelos disponibles:")
        for _vuelo in vuelos_1.Vuelos:
            print(f"Nvuelo: {_vuelo.nvuelo}, Origen: {_vuelo.origen}, Destino: {_vuelo.destino}, Fecha: {_vuelo.fecha}, Hora: {_vuelo.hora}, Avion asignado: {_vuelo._avion}")    

vuelos_1= Vuelos()

avion_17 = Avion("bartolome 14", 60)
avion_18 = Avion("bartolome 15", 60)
avion_183 = Avion("bartolome 16", 60)
avion_184 = Avion("bartolome 17", 60)
avion_185 = Avion("bartolome 18", 60)
vuelo_1 = vuelo(1,"santiago", "miami", "17/08/24", "17:40",avion_17)
vuelo_12 = vuelo(1,"santiago", "miami", "17/08/24", "17:40",avion_18)
vuelo_13 = vuelo(1,"santiago", "miami", "17/08/24", "17:40",avion_183)
vuelo_14 = vuelo(1,"santiago", "miami", "17/08/24", "17:40",avion_184)

vuelos_1.Vuelos_disponibles(vuelo_1)
vuelos_1.Vuelos_disponibles(vuelo_12)
vuelos_1.Vuelos_disponibles(vuelo_13)
vuelos_1.Vuelos_disponibles(vuelo_14)
Vuelos.mostrar_vuelos(vuelo_1)



