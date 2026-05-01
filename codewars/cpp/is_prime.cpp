#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int n){
    bool result = true;
    if (n < 2) return false;
    // by definition of prime numbers in discrete math, checking below its root is enough to prove.
    // this reduces maximum amount from 2147483647 (2^31) -> 2^15,5 = 32768 * 1,41 ~ 46200 (4,6 * 10^5)
    int sufficient_part = sqrt(n);
    for (int i = 2; i <= sufficient_part; ++i){
        if (n % i == 0) return false;
    }
    return true;
}
// test case
int main(){
    for (int i = 0; i < 7; ++i){
        cout << i << ": " << isPrime(i) ? "true" : "false";
        cout << endl;
    }
    return 0;
}