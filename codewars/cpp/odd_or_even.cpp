#include <iostream>
#include <vector>
using namespace std;

string odd_or_even(const vector<int>& arr){
    int sum = 0;
    for (int i: arr) sum += i;
    return ((sum & 1) == 0) ? "even": "odd";
}

// test case
int main(){
    vector<int> arr1 = {0, 1, 4, 9, 16};
    cout << odd_or_even(arr1) << endl;
}