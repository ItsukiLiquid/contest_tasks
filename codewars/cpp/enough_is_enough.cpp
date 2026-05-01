#include <iostream>
#include <vector>
#include <map>
using namespace std;

vector<int> deleteNth(vector<int> elements, int n){
    map<int, int> count_map;
    vector<int> result;
    for (int element: elements){
        if (count_map[element] < n){
            count_map[element] += 1;
            result.push_back(element);
        }
    }
    return result;
}

// test case

int main(){
    vector<int> elements = {1,1,3,3,7,2,2,2,2};
    int n = 3;
    vector<int> vector = deleteNth(elements, n);
    for (int num: vector) cout << num << " ";
    return 0;
}