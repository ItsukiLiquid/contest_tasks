#include <iostream>
using namespace std;

int sum_of_multipliers(int n){
    int result = 0;
    if (n > 2){
        for (int i = 2; i < n; ++i){
            if (i % 3 == 0 || i % 5 == 0) result += i;
        }
    }
    return result;
}

int main(){
    int n = 10;
    cout << sum_of_multipliers(n);
}