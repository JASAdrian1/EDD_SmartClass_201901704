#include "Tarea.h"
#include<iostream>
#include<fstream>
#include<string>
#include<Error.h>
#include<regex>
#include<ListaTareas.h>

int identificador = 0;
ListaTareas *listaT = new ListaTareas();
Tarea *tareasArray[5][30][9];

Tarea::Tarea(int mes, int dia, int hora, string carnet, string nombre, string descripcion, string materia, string fecha, string estado){
    this->mes = mes;
    this->dia = dia;
    this->hora = hora;
    this->mes = mes;
    this->carnet = carnet;
    this->nombre = nombre;
    this->descripcion = descripcion;
    this->materia = materia;
    this->fecha = fecha;
    this->estado = estado;
    identificador++;
    this->id = to_string(identificador);
}


Tarea::Tarea()
{
    //ctor
    this->id = "-1";
    this->mes = -1;
    this->dia = -1;
    this->hora = -1;
    this->mes = -1;
    this->carnet ="-1";
    this->nombre = "-1";
    this->descripcion = "-1";
    this->materia = "-1";
    this->fecha = "-1";
    this->estado = "-1";

}

void Tarea::cargarTareas(){


    for(int i=0;i<5;i++){
        for(int j=0;j<30;j++){
            for(int k=0;k<9;k++){
                tareasArray[i][j][k] = new Tarea();
            }
        }
    }


    ifstream archivo;
    string ruta;
    cout<<"Ingrese la ruta del archivo: ";
    cin.ignore();
    getline(cin,ruta);
    archivo.open(ruta,ios::in);
    if (archivo.good()){
        string linea;
        int contEnc = 0;
        while(getline(archivo,linea)){
            string del = ",";
            int start = 0;
            int endS = linea.find(del);
            int contador = 0;
            //VARIABLES PARA ALMACENAR LA INFORMACION DEL USUARIO
            string id = "0";
            string carnet = "";
            string nombre = "";
            string descripcion = "";
            string materia = "";
            string fecha = "";
            int mes = 0;
            int dia = 0;
            int hora = 0;
            string estado = "";
            if(contEnc>0){
                while (endS != -1) {
                    switch(contador){
                        case 0:
                            mes = stoi(linea.substr(start, endS - start));
                            cout<<"Mes: "<<mes<<endl;
                            break;
                        case 1:
                            dia = stoi(linea.substr(start, endS - start));
                            cout<<"Dia: "<<dia<<endl;
                            break;
                        case 2:
                            hora = stoi(linea.substr(start, endS - start));
                            cout<<"Hora: "<<hora<<endl;
                            break;
                        case 3:
                            carnet = linea.substr(start, endS - start);
                            cout<<"Carnet: "<<carnet<<endl;
                            break;
                        case 4:
                            nombre = linea.substr(start, endS - start);
                            cout<<"Nombre: "<<nombre<<endl;
                            break;
                        case 5:
                            descripcion = linea.substr(start, endS - start);
                            cout<<"Descripcion: "<<descripcion<<endl;
                            break;
                        case 6:
                            materia = linea.substr(start, endS - start);
                            cout<<"Materia: "<<materia<<endl;
                            break;
                        case 7:
                            fecha = linea.substr(start, endS - start);
                            cout<<"Fecha: "<<fecha<<endl;
                            break;

                    }
                    start = endS + del.size();
                    endS = linea.find(del, start);
                    contador+=1;

                }
                //Agregar try-catch al arreglo por si vienen fechar fuera del limite
                estado = linea.substr(start, endS - start);
                Tarea *tarea = new Tarea(mes, dia, hora, carnet, nombre, descripcion, materia, fecha, estado);
                //Se agrega la tarea al arreglo estatico de tareas
                tareasArray[mes-7][dia-1][hora-8] = tarea;
                if(hora<8 || hora>16){
                    Error *err = new Error("Tarea","Hora de la tarea fuera de rango",tarea);
                    Error::insetarError(err);
                }else if(mes<7 || mes>11){
                    Error *err = new Error("Tarea","Mes de la tarea fuera de rango",tarea);
                    Error::insetarError(err);
                }else if(dia<1 || mes>30){
                    Error *err = new Error("Tarea","Dia de la tarea fuera de rango",tarea);
                    Error::insetarError(err);
                }
                if(!this->validarFormatoFehca(tarea->fecha)){
                    Error *err = new Error("Tarea","Formato de la fecha invalido",tarea);
                    Error::insetarError(err);
                }
            }
            contEnc+=1;

        }
        Error::imprimirColaError();


        cout<<"hola"<<endl;
        cout<<tareasArray[3][3][1]->id<<endl;
        cout<<typeid(tareasArray[1][0][1]).name()<<endl;
        //cout<<tareasArray[0][13][2]->id<<endl;
        /*for(int i =0;i<5;i++){
            for(int j=0;j<30;j++){
                cout<<"****************************"<<endl;
                cout<<j+1<<"/"<<i+7<<"/"<<2021<<endl;
                for(int k=0;k<9;k++){
                    if(tareasArray[i][j][k]->id !="-1"){
                        cout<<"Hora: "<<k+8<<endl;
                        cout<<"Id: "<<tareasArray[i][j][k]->id<<endl;
                        cout<<"Carnet: "<<tareasArray[i][j][k]->carnet<<endl;
                        cout<<"Nombre: "<<tareasArray[i][j][k]->nombre<<endl;
                        cout<<"Descripcion: "<<tareasArray[i][j][k]->descripcion<<endl;
                        cout<<"Materia: "<<tareasArray[i][j][k]->materia<<endl;
                        cout<<"Estado: "<<tareasArray[i][j][k]->estado<<endl;
                    }
                }
                cout<<"****************************"<<endl;
            }
        }*/

        //Se realiza la linealizacion de las tareas
        int contadorCal = 0;
        for(int i =0;i<9;i++){
            for(int j=0;j<30;j++){
                for(int k=0;k<5;k++){
                    tareasArray[k][j][i]->id = to_string(contadorCal);
                    listaT->insertar(tareasArray[k][j][i]);
                    contadorCal+=1;
                    if(tareasArray[k][j][i]->materia!="-1"){
                        cout<<"****************************"<<endl;
                        cout<<tareasArray[k][j][i]->id<<endl;
                        cout<<tareasArray[k][j][i]->nombre<<endl;
                        cout<<"****************************"<<endl;
                    }
                }
            }
        }
        //listaT->imprimirTareas();


        printf("Se ha cargado el archivo correctamente");

    }else{
        cout<<"No se ha encontrado el archivo"<<endl;
    }

}


void Tarea::busquedaLinealizada(int posicion){
    listaT->busquedaLinealizada(posicion);
}

bool Tarea::validarFormatoFehca(string fecha){
    const regex expReg("(\\d){4}/(\\d){2}/(\\d){2}");
    //cout<<regex_match(fecha,expReg)<<endl;
    return regex_match(fecha,expReg);
}

void Tarea::graficarLista(){
    listaT->graficarLista();
}

string Tarea::generarCodigoSalida(){
    return listaT->generarCodigoSalida();
}

Tarea::~Tarea()
{
    //dtor
}
