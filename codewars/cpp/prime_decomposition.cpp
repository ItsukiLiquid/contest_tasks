#include <iostream>
#include <map>
#include <cmath>
using namespace std;

class PrimeDecomp{
public:
    static string factors(int number){
        int modifiable_number = number;
        string result = "";
        map<int, int> factors_quantity;
        int sufficient_quotient = sqrt(modifiable_number);
        for (int i = 2; i <= sufficient_quotient; ++i){
            while (modifiable_number % i == 0){
                factors_quantity[i] += 1;
                modifiable_number /= i;
                // cout << modifiable_number << endl;
            }
        }
        factors_quantity[modifiable_number] = 1;
        for (pair<int, int> factor_info: factors_quantity){
            // cout << factor_info.first << " " << factor_info.second << endl;
            if (factor_info.first != 1){
                if (factor_info.second == 1) result = result + '(' + to_string(factor_info.first) + ')';
                else result = result + '(' + to_string(factor_info.first) + "**" + to_string(factor_info.second) + ')';
            }
        //     if (factor_info.first == 1) continue;
        //     else if (factor_info.second == 1) result = result + '(' + to_string(factor_info.first) + ')';
        //     else {
        //         // if (modifiable_number == 1) result = result + '(' + to_string(factor_info.first) + "**" + to_string(factor_info.second) + ')';
        //         result = result + '(' + to_string(factor_info.first) + "**" + to_string(factor_info.second) + ")(" + to_string(modifiable_number) + ')';
        //     }
        }
        return result;
    }
};

int main(){
    PrimeDecomp p;
    int number; cin >> number;
    cout << endl << p.factors(number);
    return 0;
}