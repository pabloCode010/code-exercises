// COMPARE THE TRIPLETS
// https://www.hackerrank.com/challenges/compare-the-triplets/problem?isFullScreen=false

// Alice y Bob crearon cada uno un problema para HackerRank. Un revisor califica los dos desafíos y otorga puntos en una escala del 1 al 100 para tres categorías: claridad del problema , originalidad y dificultad .

// La calificación para el desafío de Alice es el triplete a = (a[0], a[1], a[2]) y la calificación para el desafío de Bob es el triplete b = (b[0], b[1], b [2]) .

// La tarea es encontrar sus puntos de comparación comparando a[0] con b[0] , a[1] con b[1] y a[2] con b[2] .

// Si a[i] > b[i] , Alice recibe 1 punto.
// Si a[i] < b[i] , Bob recibe 1 punto.
// Si a[i] = b[i] , ninguna persona recibe un punto.
// Los puntos de comparación son los puntos totales que obtuvo una persona.

// Dados a y b , determine sus respectivos puntos de comparación.

#include <iostream>
#include <vector>
using namespace std;

vector<int> compareTriplets(vector<int> a, vector<int> b) {
    vector<int> result;
    result.push_back(0);
    result.push_back(0);
    for (int i = 0; i < 3; i++){
        if(a[i] > b[i]){
            result[0] += 1;
        }else if(b[i] > a[i]){
            result[1] += 1;
        }
    }
    return result;
    
}

int main () {
    vector<int> bob;
    vector<int> alice;
    vector<int> result;

    bob.push_back(17);
    bob.push_back(28);
    bob.push_back(30);

    alice.push_back(99);
    alice.push_back(16);
    alice.push_back(8);

    result = compareTriplets(alice, bob);
    cout << result[0] << " " << result[1];

    return 0;
}