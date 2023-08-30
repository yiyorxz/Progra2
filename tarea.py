class avion:
    def __init__(self,modelo,asientos):
        self.modelo = modelo
        self.asientos = asientos
class vuelo:
    def __init__(self,numero_vuelo,origen, destino, fecha, hora):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino= destino
        self.fecha = fecha
        self.hora = hora
        self.avion = avion
        self.reserva= []

class pasajero:
    def __init__(self,nombre,npasaporte):
        self.nombre= nombre
        self.npasaporte = npasaporte
        self.reservas=[]
class reservacion:
    def __init__(self,pasajero,vuelo,estado):
        self.pasajero = pasajero
        self.vuelo= vuelo
        self.estado= estado
class vuelosdispo:
    def __init__(self):
        self.vuelosdispo=[]
    def agregavuelos(self,_vuelo):
        vuelosdispo=[]
        if not isinstance(_vuelo, vuelo):
            print("no se puede agregar este vuelo")
            return
        vuelosdispo.append(_vuelo)
        print (vuelosdispo)
####################################################################################################################
vuelo1 = vuelo(int(input('inserte numero vuelo ')),str(input('inserte origen ')),str(input('inserte destino ')),str(input('inserte fecha ')),str(input('inserte hora ')))
vuelosdisp=vuelosdispo()
vuelosdisp.agregavuelos(vuelo1)

        