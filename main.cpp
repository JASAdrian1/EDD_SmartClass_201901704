#include <iostream>
#include<Usuarios.h>
#include<string>
#include<conio.h>
#include<Usuarios.h>
#include<Tarea.h>
#include<Error.h>

using namespace std;

void menu();

int main()
{
    menu();
    return 0;
}


void menu(){
    Usuarios *usuarios = new Usuarios();
    Tarea *tareas = new Tarea();
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
            }else if(opcionReporte == "5"){
                Error::graficarErrores();
            }

        }else if(opcion == "5"){
            cout<<"Presione enter para finalizar el programa"<<endl;
            getch();
            break;
        }else{
            cout<<"No ha ingresado una opcion valida"<<endl;
            getch();
        }
    }

}
