#include <iostream>
#include <vector>
using namespace std;

pair<int, int> two_sum(const vector<int>& numbers, int target){
    for (int i = 0; i < numbers.size(); ++i){
        for (int j = 0; j < numbers.size(); ++j){
            if (numbers[i] + numbers[j] == target && i != j){
                return make_pair(i, j);
            }
        }
    }
}

// test case
int main(){
    vector<int> numbers = {1, 2, 3, 4, 5};
    int target = 7;
    pair<int, int> result = two_sum(numbers, target);
    cout << "Indices: " << result.first << ", " << result.second << endl;
}