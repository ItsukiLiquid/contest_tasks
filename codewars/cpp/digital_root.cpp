#include <iostream>
using namespace std;

int digital_root(int n){
    if (n < 10) return n;
    int result = n % 10 + digital_root(n / 10);
    if (result >= 10) return result % 10 + digital_root(result / 10);
    return result;
}

int main(){
    int n = 67;
    cout << digital_root(n);
    return 0;
}