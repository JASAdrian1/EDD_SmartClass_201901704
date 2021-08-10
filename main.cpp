#include <iostream>
#include<Usuarios.h>
#include<string>

using namespace std;

void menu();

int main()
{
    menu();
    return 0;
}


void menu(){
    string opcion ="";
    printf("Menu");
    printf("\n1. Carga de usuarios");
    printf("\n2. Carga de tareas");
    printf("\n3. Ingreso manual");
    printf("\n4. Reportes");
    printf("\nIngrese el numero de la opcion a la que desea ingresar: ");
    cin>>opcion;
    if(opcion == "1"){
        Usuarios::cargarUsuarios();
    }
}

