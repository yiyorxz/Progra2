from datetime import datetime
class Avion:
    def __init__(self, modeloavion, asientos):
        self.modeloavion = modeloavion
        self.asientos = asientos
    def __str__(self):
        return f"{self.modeloavion} {self.asientos}"    
class vuelo:
     def __init__(self, nvuelo, origen, destino, fecha, hora , _avion ):
         self.nvuelo = nvuelo
         self.origen=origen
         self.destino= destino
         self.fecha= fecha
         self.hora=hora
         self._avion=_avion
         self.reservaciones=[]
     def __str__(self):
        return f"{self.nvuelo}, {self.origen}, {self.destino}, {self.fecha}, {self.hora} {self._avion}"  
     def reservar(self,_reserva):
        self.reservaciones.append(_reserva)
     def mostrar_reservas(_reserva):
        print("reservas:")
        for _reserva in vuelo.reservaciones:
            print(f"numero reserva {_reserva.nreserva} (Pasajero: {_reserva._pasajero}), (Vuelo: {_reserva._vuelo}) Estado: {_reserva.estado}")
class Vuelos:
    def __init__(self):
        self.Vuelos = []

    def Vuelos_disponibles(self, avuelo):
        self.Vuelos.append(avuelo)


    def mostrar_vuelos(_vuelo):
        print("Vuelos disponibles:")
        for _vuelo in vuelos_1.Vuelos:
            print(f"vuelo: {_vuelo.nvuelo}, Lugar de Origen: {_vuelo.origen}, Lugar de Destino: {_vuelo.destino}, Fecha asignada: {_vuelo.fecha}, Hora de: {_vuelo.hora}, Avion asignado: {_vuelo._avion}"
                  "-------------------------------------------------------------------------------------------------------------------------------------------------------------------------")    
class Pasajero:
    def __init__(self, pasaporte, nombre):
        self.pasaporte = pasaporte
        self.nombre = nombre
        self.vuelos_reservados = []
    def __str__(self):
        return f"{self.pasaporte}, {self.nombre}"
class reservacion:
    def __init__(self, nreserva, _pasajero, _vuelo, estado):
        self.nreserva=nreserva
        self._pasajero=_pasajero
        self._vuelo=_vuelo
        self.estado=estado
listaaviones=[]
def crear_aviones(x):
    listaaviones=[]
    for l in range(x):
        listaaviones.append(l)
    for i in range(0,x):
        listaaviones[i-1]= Avion(str(input("ingrese nombre avion ")), str(input("ingrese numero de asientos ")))
    print("aviones disponibles: ")
    for c in range(len(listaaviones)):
        print (f"Nombre del avion '{listaaviones[c].modeloavion}' Numero de asientos '{listaaviones[c].asientos}'")
    return listaaviones

def crear_vuelos(x):
    listavuelos=[]
    for i in range(x):
        listavuelos.append(i)
    for l in range(0,x):
        listavuelos[l]=vuelo(input("Ingrese numero de vuelo "),input("Ingrese lugar de origen"),input("Ingrese lugar de destino"),input("Ingrese fecha "),input("ingrese hora "),input(listaaviones[l-1]))

        
crear_aviones(3)
crear_vuelos(3)
aaaaaa


        


