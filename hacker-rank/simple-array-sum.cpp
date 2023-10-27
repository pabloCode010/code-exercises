// SIMPLE ARRAY SUM
// https://www.hackerrank.com/challenges/simple-array-sum/problem?isFullScreen=true

// Dado un conjunto de números enteros, encuentre la suma de sus elementos.
// Por ejemplo, si la matriz es [1,2,3] regresa 1 + 2 + 3.

#include <iostream>
#include <vector>
using namespace std;

int simpleArraySum(vector<int> ar) {
    int sum = 0, length = ar.size();
    
    for (int i=0; i < length; i++) {
        sum += ar[i];
    }
    
    return sum;
}

int main(){
    vector<int> myVector;
    int sum;

    myVector.push_back(10);
    myVector.push_back(20);
    myVector.push_back(30);
    myVector.push_back(40);

    sum = simpleArraySum(myVector);

    cout << "Result: " << sum << endl; 

    return 0;
}