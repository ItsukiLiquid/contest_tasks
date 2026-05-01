#include <iostream>
#include <cmath>
using namespace std;

bool narcissistic(int n){
    string s = to_string(n);
    int sum = 0;
    for (char c: s){
        int digit = c - int('0');
        sum += pow(digit, s.size());
    }
    return (sum == n) ? true : false;
}

// test case
int main(){
    int n1 = 153;
    int n2 = 154;
    cout << narcissistic(n1) << endl;
    cout << narcissistic(n2) << endl;
}