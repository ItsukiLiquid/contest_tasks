#include <iostream>
using namespace std;

class Solution {
public:
    string reverse_number(int x){
        string s = to_string(x);
        for (int i = 0; i < s.size(); ++i){
            if (s[i] == '-') continue;
            s[i] = s[s.size() - 1 - i];
        }
        return s;
    }
    bool isPalindrome(int x){
        if (x < 0) return false;
        string s = to_string(x);
        string reversed_s = reverse_number(x);
        return (s == reversed_s) ? true: false;

    }
};