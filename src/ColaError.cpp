#include "ColaError.h"
#include<Error.h>
#include<NodoError.h>
#include<fstream>
#include<conio.h>

ColaError::ColaError()
{
    //ctor
    this->primero = nullptr;
    this->tamanio = 0;
}

int ColaError::estaVacia(){
    return this->primero == nullptr;
}

void ColaError::encolar(Error *err){
    NodoError *nuevo = new NodoError(err,nullptr);
    if(this->estaVacia()){
            this->primero = nuevo;
    }else{
        //cout<<"Hola"<<endl;
        NodoError *tmp = this->primero;
        while(tmp->siguiente!=nullptr){
            tmp = tmp->siguiente;

        }
        tmp->siguiente = nuevo;
    }
}

void ColaError::desencolar(){
    if(!this->estaVacia()){
        NodoError *aux = this->primero;
        this->primero = this->primero->siguiente;
        delete(primero);
    }else{
        cout<<"La pila de errores está vacia";
    }
}


void ColaError::mostrarCola(){
    if(!this->estaVacia()){
        NodoError * tmp = this->primero;
        while(tmp!=nullptr){
            cout<<"**********************"<<endl;
            cout<<"Id: "<<tmp->err->id<<endl;
            cout<<"Tipo: "<<tmp->err->tipo<<endl;
            cout<<"Descripcion: "<<tmp->err->descripcion<<endl;
            cout<<"**********************"<<endl;
            tmp = tmp->siguiente;
        }
    }else{
        cout<<"La pila de errores esta vacia"<<endl;
    }
}

int contGraficasErrores;
void ColaError::graficarErrores(){
    contGraficasErrores+=1;
    if(!this->estaVacia()){
        ofstream fs("graficaColaErrores"+to_string(contGraficasErrores)+".dot");
        fs<<"digraph g {"<<endl;
        fs<<"rankdir=LR;"<<endl;
        fs<<"node[shape=circle];"<<endl;
        int contador = 0;
        NodoError *tmp = this->primero;
        while(tmp->siguiente!=nullptr){
            string info = "ID:"+to_string(tmp->err->id)+"\\nTipo: "+tmp->err->tipo+
            "\\nDescripcion: "+tmp->err->descripcion;
            fs<<contador<<"[label=\""<<info<<"\"];"<<endl;
            contador+=1;
            tmp = tmp->siguiente;
        }
        //Se crea el ultimo nodo de la grafica
        string info = "ID:"+to_string(tmp->err->id)+"\\nTipo: "+tmp->err->tipo+
            "\\nDescripcion: "+tmp->err->descripcion;
        fs<<contador<<"[label=\""<<info<<"\"];"<<endl;

        for(int i=0;i<contador;i++){
            fs<<i<<"->"<<i+1<<endl;
        }
        fs<<"}"<<endl;
        cout<<"Se ha creado la grafica exitosamente"<<endl;
        fs.close();
        string nombreGraficaErrores = "graficaColaErrores"+to_string(contGraficasErrores);
        system(("dot -Tsvg "+nombreGraficaErrores+".dot -o "+nombreGraficaErrores+".svg").c_str() );
        system((nombreGraficaErrores+".png").c_str() );
        getch();
    }
}

ColaError::~ColaError()
{
    //dtor
}
