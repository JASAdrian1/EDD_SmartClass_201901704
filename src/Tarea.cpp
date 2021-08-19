#include "Tarea.h"
#include<iostream>
#include<fstream>
#include<string>

int identificador = 0;

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
    this->id = "-1";
    this->mes = 0;
    this->dia = 0;
    this->hora = 0;
    this->mes = 0;
    this->carnet = "";
    this->nombre = "";
    this->descripcion = "";
    this->materia = "";
    this->fecha = "";
    this->estado = "";
    //ctor
}

void Tarea::cargarTareas(){
    Tarea *tareasArray[5][30][9];


    /*tareasArray = new Tarea ***[5];
    for(int i=0;i<5;i++){
        tareasArray[i] = new Tarea**[30];
    }
    for(int i=0;i<5;i++){
        for(int j=0;j<30;j++){
            tareasArray[i][j] = new Tarea*[8];
        }
    }*/


    //Inicialiar tareas
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
                estado = linea.substr(start, endS - start);
                Tarea *tarea = new Tarea(mes, dia, hora, carnet, nombre, descripcion, materia, fecha, estado);
                tareasArray[mes-7][dia-1][hora-8] = tarea;

            }
            contEnc+=1;
            //cout<<contador;

        }
        cout<<"hola"<<endl;
        cout<<tareasArray[3][3][1]->id<<endl;
        cout<<typeid(tareasArray[1][0][1]).name()<<endl;
        //cout<<tareasArray[0][13][2]->id<<endl;
        for(int i =0;i<5;i++){
            for(int j=0;j<30;j++){
                cout<<"****************************"<<endl;
                cout<<j+1<<"/"<<i+7<<"/"<<2021<<endl;
                for(int k=0;k<9;k++){
                    if (tareasArray[i][j][k]->id != "-1"){
                        cout<<"Hora: "<<k+8<<endl;
                        cout<<tareasArray[i][j][k]->materia<<endl;
                    }
                }
                cout<<"****************************"<<endl;
            }
        }

        //listaUs->imprimirUsuarios();

        printf("Se ha cargado el archivo correctamente");

    }else{
        cout<<"No se ha encontrado el archivo"<<endl;
    }

}


Tarea::~Tarea()
{
    //dtor
}
