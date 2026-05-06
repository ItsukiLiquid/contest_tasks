#include <iostream>
#include <string>
using namespace std;
class Add {
public:
    int value;
    Add(int s) : value(s) {}
    Add operator()(int s) {
        return Add(value + s);
    }
};

int main() {
    Add add(7);
    cout << add(3).value << endl; // 10
    cout << add(3)(4).value << endl; // 14
    cout << add(3)(4)(5).value << endl; // 19
    return 0;
}