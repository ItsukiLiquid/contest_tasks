#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

class Tortoise
{
public:
    static vector<int> race(int v1, int v2, int g){
        vector<int> result(3);
        if (v1 >= v2) return {-1, -1, -1};
        int diff_v = v2 - v1; // ft/h -> some ft / 3600s
        // 720, 850, 70 -> diff 130 ft/h -> 130 ft / 3600s -> 70 ft. then s = 70 * 3600 / 130 = 1938 sec
        int total_time = round(g * 3600 / diff_v);
        int time_hour = total_time / 3600;
        int time_min = total_time / 60 - 60 * time_hour;
        int time_sec = total_time - 60 * time_min - 3600 * time_hour;
        result[0] = time_hour;
        result[1] = time_min;
        result[2] = time_sec;
        return result;
    }
};

int main(){
    int v1, v2, g; cin >> v1 >> v2 >> g;
    Tortoise t;
    vector<int> race_time = t.race(v1, v2, g);
    for (int timestamp: race_time) cout << timestamp << " ";
    return 0;
}