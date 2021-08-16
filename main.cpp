#include <iostream>
#include<Usuarios.h>
#include<string>
#include<conio.h>

using namespace std;

void menu();

int main()
{
    menu();
    return 0;
}


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
            Usuarios::cargarUsuarios();
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
                    Usuarios::insertarUsuario();
                }else if(opcionUsuarios == "2"){
                    Usuarios::modificarUsuario();
                }else if(opcionUsuarios == "3"){
                    Usuarios::eliminarUsuario();
                }
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

