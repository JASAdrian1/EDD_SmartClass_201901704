#include <iostream>
#include<Usuarios.h>
#include<string>
#include<conio.h>
#include<Usuarios.h>
#include<Tarea.h>
#include<Error.h>
#include <fstream>

using namespace std;

void reporteCodigoSalida();

void menu();

int main()
{
    menu();
    return 0;
}

Usuarios *usuarios = new Usuarios();
Tarea *tareas = new Tarea();

void menu(){

    string opcion ="";
    while (opcion !="5"){
        printf("Menu");
        printf("\n1. Carga de usuarios");
        printf("\n2. Carga de tareas");
        printf("\n3. Ingreso manual");
        printf("\n4. Reportes");
        printf("\n5. Salir");
        printf("\nIngrese el numero de la opcion a la que desea ingresar: ");
        cin>>opcion;
        if(opcion == "1"){
            usuarios->cargarUsuarios();

        }else if(opcion == "2"){
            tareas->cargarTareas();

        }else if(opcion == "3"){
            string opcionSub ="";
            cout<<"1. Usuarios"<<endl;
            cout<<"2. Tareas"<<endl;
            cout<<"3. Salir"<<endl;
            printf("Ingrese el numero de la opcion a la que desea ingresar: ");
            cin >> opcionSub;
            if(opcionSub == "1"){
                string opcionUsuarios ="";
                cout<<"MENU USUARIOS"<<endl;
                cout<<"1. Ingresar"<<endl;
                cout<<"2. Modificar"<<endl;
                cout<<"3. Eliminar"<<endl;
                cout<<"4. Salir"<<endl;
                printf("Ingrese el numero de la opcion que desea ejecutar: ");
                cin >> opcionUsuarios;
                if(opcionUsuarios == "1"){
                    usuarios->insertarUsuario();
                }else if(opcionUsuarios == "2"){
                    usuarios->modificarUsuario();
                }else if(opcionUsuarios == "3"){
                    usuarios->eliminarUsuario();
                }
            }
        //Opciones para los reportes
        }else if(opcion == "4"){
            string opcionReporte = "";
            cout<<"1. Lista de estudiantes"<<endl;
            cout<<"2. Lista de tareas linealizadas "<<endl;
            cout<<"3. Busqueda en estructura linealizada"<<endl;
            cout<<"4. Busqueda de posicion en lista linealizada"<<endl;
            cout<<"5. Cola de errores"<<endl;
            cout<<"6. Codigo generado de salida"<<endl;
            cout<<"Ingrese el numero de la opcion que desea ejecutar"<<endl;
            cin>>opcionReporte;
            if(opcionReporte == "1"){
                usuarios->graficarLista();
            }else if(opcionReporte == "2"){
                tareas->graficarLista();
            }else if(opcionReporte == "3"){
                int mes=0; int dia=0; int hora=0; int indice=0;
                cout<<"Ingrese el mes: "; cin>>mes;
                cout<<"Ingrese el dia: "; cin>>dia;
                cout<<"Ingrese la hora: "; cin>>hora;
                indice = ((hora-8)*30 + dia-1)*5+mes-7;
                tareas->busquedaLinealizada(indice);
            }else if(opcionReporte =="4"){
                int mes=0; int dia=0; int hora=0; int indice=0;
                cout<<"Ingrese el mes: "; cin>>mes;
                cout<<"Ingrese el dia: "; cin>>dia;
                cout<<"Ingrese la hora: "; cin>>hora;
                indice = ((hora-8)*30 + dia-1)*5+mes-7;
                if (indice>=0){
                    cout<<"La tarea se encuentra en la posicion "<<indice<<" de la lista linealizada."<<endl;
                }else{
                    cout<<"No se ha encontrado la tarea en la lista"<<endl;
                }

                getch();
            }else if(opcionReporte == "5"){
                Error::graficarErrores();
            }else if(opcionReporte == "6"){
                reporteCodigoSalida();
            }

        }else if(opcion == "5"){
            cout<<"Presione cualquier tecla para finalizar el programa"<<endl;
            getch();
            break;
        }else{
            cout<<"No ha ingresado una opcion valida"<<endl;
            getch();
        }
    }

}




void reporteCodigoSalida(){
    ofstream fs("codigoSalida.txt");
    fs<<"¿Elements?"<<endl;
    fs<<usuarios->generarCodigoSalida();
    fs<<tareas->generarCodigoSalida();
    fs<<"¿$Elements?"<<endl;
    fs.close();
    cout<<"Se ha generado el codigo de salida exitosamente"<<endl;
    getch();
}
