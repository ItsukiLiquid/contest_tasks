#include <iostream>
using namespace std;

string add_binary(size_t a, size_t b){
    string result = "";
    size_t converting_number = a + b;
    while (converting_number){
        result = to_string(converting_number % 2) + result;
        converting_number /= 2;
    }
    return (a + b == 0) ? "0" : result;
}

// test case
int main(){
    size_t a = 1000000000;
    size_t b = 1147483647;
    cout << add_binary(a, b) << endl; // 1111111111111111111111111111111 1111111111111111111111111111111
}