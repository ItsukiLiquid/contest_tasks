#include <iostream>
#include <string>
using namespace std;
class Accumul
{
public:
    static char to_upper(char c){
      if (c >= int('a') && c <= int('z')){
        char result = char(int(c) - int('a') + int('A'));
          return result;
      }
      return c;
    }
    static char to_lower(char c){
        if (c >= int('A') && c <= int('Z')){
          char result = char(int(c) - int('A') + int('a'));
            return result;
        }
        return c;
      }
    static string accum(const string &s){
      string result = "";
      for (int i = 0; i < s.size(); ++i){
        char current_char = s[i];
        for (int j = 0; j <= i; ++j){
            if (j == 0) result = result + to_upper(current_char);
            else result = result + to_lower(current_char);
          }
        if (i != s.size() - 1) result = result + '-';
        }
      return result;
      }
  };