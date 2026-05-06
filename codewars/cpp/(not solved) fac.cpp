#include <iostream>
#include <string>
using namespace std;

long long fac(int n){
    if (n == 0 || n == 1) return 1;
    return n * fac(n - 1);
}

string factorial(int n){
    long long result = fac(n);
    return to_string(result);
}

int main(){
    int n = 7;
    cout << factorial(n);
    return 0;
}