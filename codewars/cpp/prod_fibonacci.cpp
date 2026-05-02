#include <iostream>
using namespace std;
#include <vector>
typedef unsigned long long ull;
class ProdFib
{
public:
    static size_t fibonacci(int n){
        if (n == 0) return 0;
        if (n == 1) return 1;
        else if (n <= -1) return -1;
        else return fibonacci(n - 1) + fibonacci(n - 2);
    }
    static vector<ull> productFib(ull prod){
        vector<ull> result = {0, 0, false};
        int n = 0;
        // fib0 = 0, fib1 = 1, fib2 = 1, fib3 = 2, fib4 = 3 ...
        while (fibonacci(n) * fibonacci(n + 1) <= prod){
            if (fibonacci(n) * fibonacci(n + 1) == prod){
                result[0] = fibonacci(n);
                result[1] = fibonacci(n + 1);
                result[2] = true;
                return result;
            }
            n += 1;
        }
        if (fibonacci(n) * fibonacci(n + 1) > prod){
            result[0] = fibonacci(n);
            result[1] = fibonacci(n + 1);
            return result;
        }
    }
};

// test case

int main(){
    ull prod; cin >> prod;
    ProdFib pf;
    vector<ull> result = pf.productFib(prod);
    for (ull element: result) cout << element << " ";
    return 0;
}