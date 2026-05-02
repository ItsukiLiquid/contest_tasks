#include <iostream>
#include <string>
#include <vector>
#include <cctype>
using namespace std;


vector<string> wave(string str){
    vector<string> result;
    for (int i = 0; i < str.size(); ++i){
        string current_str = str;
        if (current_str[i] != ' '){
            current_str[i] = toupper(current_str[i]);
            result.push_back(current_str);
        }
    }
    return result;
}

int main(){
    string a; cin >> a;
    vector<string> waved = wave(a);
    for (string word: waved) cout << word << " ";
    return 0;
}