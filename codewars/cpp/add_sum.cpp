#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int ctoi(const char c){
    if (int(c) >= int('0') && int(c) <= int('9')) return int(c) - int('0');
    else if (!c) return 0;
}

long long string_to_int(const string a){
    long long result = 0;
    for (int i = a.size() - 1; i >= 0; --i){
        // example for 567
        // 0 + 7 * pow(10, 0) => 7
        // 7 + 6 * pow(10, 1) => 7 + 60 = six seveen 67
        // 67 + 5 * pow(10, 2) => 67 + 500 = 567
        // let a = 567, a.size() = 3
        // i = 2 -> 1 -> 0 (a.size() - 1 => 0)
        // pow(10, j) j = 0 -> 1 -> 2 a.size() - i - 1 = (3 - 2 - 1 => 0), (3 - 1 - 1 => 1), (3 - 0 - 1 => 2)
        result = result + ctoi(a[i]) * pow(10, a.size() - i - 1);
    }
    return result;
}

// string add(const string& a, const string& b) {
//     long long n1 = string_to_int(a);
//     long long n2 = string_to_int(b);
//     long long result = n1 + n2;
//     return to_string(result);
// }


string add (const string& a, const string& b){
    string n1 = a;
    string n2 = b;
    string result = "";
    int memory_number = 0;
    int current_sum = 0;
    if (n1.size() > n2.size()){
        while (n2.size() != n1.size()) n2 = '0' + n2;
    }
    else if (n2.size() > n1.size()){
        while (n1.size() != n2.size()) n1 = '0' + n1;
    }
    // cout << n1 << " " << n2;
    for (int i = n1.size() - 1; i >= 0; --i){
        current_sum = ctoi(n1[i]) + ctoi(n2[i]) + memory_number;
        if (memory_number > 0) memory_number -= 1;
        if (current_sum >= 10) {
            int mod10 = current_sum - 10;
            result = to_string(mod10) + result;
            memory_number += 1;
            // cout << "mod10: " << mod10 << " memory number: " << memory_number << " current sum: " << current_sum << endl;
        }
        else{
            result = to_string(current_sum) + result;
        }
        // cout << "current sum: " << current_sum << endl;
        if (i == 0 && memory_number != 0) result = to_string(memory_number) + result;
    }
    return result;
}
int main(){
    string a = "167";
    string b = "67";
    cout << add(a, b);
    return 0;
}