// SOLVE ME FIRST
// https://www.hackerrank.com/challenges/solve-me-first/problem?isFullScreen=true

// Complete la función solveMeFirst para calcular la suma de dos números enteros.

// Ejemplo
// a = 3
// b = 7
// return 10



#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int solveMeFirst(int a, int b) {
  return a + b;
}

int main() {
  int num1, num2;
  int sum;
  cin>>num1>>num2;
  sum = solveMeFirst(num1,num2);
  cout<<sum;
  return 0;
}