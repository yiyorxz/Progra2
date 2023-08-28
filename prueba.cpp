#include <iostream>
#include <array>
using namespace std;
class avion {
    private:
        string modelo;
        int numero_asientos;
};
class vuelo {
    private:
        int numero_vuelo;
        string origen;
        string destino;
        string fecha;
        string hora;
        array<string, 6> reservaciones = {};
};
class pasajero {
    private:
        string nombre;
        string apellido;
        int n_pasaporte;
        array<char const*, 6> reservaciones ={};
    public:
        pasajero(string, string, int);
        void leer();
};
pasajero::pasajero(string _nombre,string _apellido,int _npasport){
    nombre= _nombre;
    apellido= _apellido;
    n_pasaporte= _npasport;
}
void pasajero::leer(){
    cout<<"soy "<<nombre<<" "<<apellido<<" y yo me vengo, y mi pasport es "<<n_pasaporte<<" "<<endl;
}


class reservacion {
    private:
        int n_reserva;

};
int main(){
    int max = 1;
    while (max <= 6){
        int x = 1;
        string nom;
        cout<<"ingrese nombre del pasajero ", cin>> nom;
        string ape;
        cout<<"ingrese apellido del pasajero ", cin>> ape;
        int pasaporte;
        cout<<"ingrese pasaporte del pasajero ", cin>> pasaporte;
        pasajero p1= pasajero(nom, ape, pasaporte);
        x +=1;
        max +=1;
        p1.leer();
        
    }

}
