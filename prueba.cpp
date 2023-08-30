#include <iostream>
#include <array>
using namespace std;
class avion {
    public:
        string modelo;
        int numero_asientos;
    public:
    avion(string,int);
};
class vuelo {
    public:
        string numero_vuelo;
        string origen;
        string destino;
        string fecha;
        string hora;
        
    public:
        vuelo(string, string,string,string, string);
        void mostrar();
};
class vuelosdisponible{
    public:
        string lista[5] = {};
    public:
        vuelosdisponible(string);
        void mostrar();
};
class pasajero {
    public:
        string nombre;
        string apellido;
        int n_pasaporte;
    public:
        pasajero(string, string, int);
};
class reservacion {
    public:
        int n_reserva;
        string pasajero;
        string vuelo;
        string estado;
    public:
        reservacion(int, string);

};
//####################################################################################################
avion::avion(string _modelo, int _nasientos){
    modelo= _modelo;
    numero_asientos= _nasientos;

}
//####################################################################################################
vuelo::vuelo(string _numero, string _origen, string _destino, string _fecha, string _hora){
    numero_vuelo= _numero;
    origen= _origen;
    destino = _destino;
    fecha= _fecha;
    hora=_hora;
}
vuelosdisponible::vuelosdisponible(string _lista){
    lista[5].append(_lista);
}
void vuelosdisponible::mostrar(){
    int tamano= 6;
    for( int i=-1; tamano>i; --i){
        cout<<lista[i]<<endl;
    }
    
}

//####################################################################################################
pasajero::pasajero(string _nombre,string _apellido,int _npasport){
    nombre= _nombre;
    apellido= _apellido;
    n_pasaporte= _npasport;
}
//####################################################################################################
reservacion::reservacion(int _nreserva, string _estado){
    n_reserva=_nreserva;
    estado= _estado;
}
int main(){
    vuelo v1= vuelo("1","toronto","Santiago","14/08/23","18:30");
    string v1;
    vuelosdisponible a1= vuelosdisponible(v1);

    int z;
    cout<<"hola",cin>>z;

}
