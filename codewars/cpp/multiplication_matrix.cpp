#include <iostream>
#include <vector>
using namespace std;

vector<vector<int> > multiplication_table(int n){
    vector<vector<int> > result(n, vector<int>(n));
    for (int i = 0; i < n; ++i){
        for (int j = 0; j < n; ++j){
            result[i][j] = (i + 1) * (j + 1);
        }
    }
    return result;
}



// 0, 0 -> 1
// 0, 1 -> 2
// 0, 2 -> 3 ... 0, n -> n + 1
// 1, 0 -> 2
// 1, 1 -> 4
// 1, 2 -> 6 ... 1, n -> (1 + 1) * (n + 1)
// 2, 0 -> 3
// 2, 1 -> 6
// 2, 2 -> 9 ... k, n -> (k + 1) * (n + 1)

int main(){
    int n = 3;
    vector<vector<int> > result = multiplication_table(n);
    for (int i = 0; i < n; ++i){
        for (int j = 0; j < n; ++j){
            cout << result[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}