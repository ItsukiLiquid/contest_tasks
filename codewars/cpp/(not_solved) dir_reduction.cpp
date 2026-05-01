#include <iostream>
#include <vector>
#include <string>
#include <cctype>
#include <map>
using namespace std;


class DirReduction
{
public:
    static string to_lower(string direction){
        string result = direction;
        for (char& c: result) c = tolower(c);
        return result;
    }
    static vector<string> dirReduc(vector<string> &arr){
        int dx = 0; // a change of direction in x axis (west / east)
        int dy = 0; // a change of direction in y axis (north / south)
        // int step = 0; <-- need for debugging
        map<string, pair<int, int> > dir_change = {
            {"north", {0, 1}},
            {"south", {0, -1}},
            {"east", {1, 0}},
            {"west", {-1, 0}}
        };
        vector<string> result;
        for (string direction: arr){
            string current_direction = to_lower(direction);
            dx = dx + dir_change[current_direction].first;
            dy = dy + dir_change[current_direction].second;
            // need for debugging
            // cout << "Step: " << step << " dx, dy: " << dx << " " << dy << endl;
            // step += 1;
        }
        while (dx != 0 || dy != 0){
            if (dx < 0){
                result.push_back("WEST");
                dx += 1;
            }
            else if (dx > 0){
                result.push_back("EAST");
                dx -= 1;
            }
            else if (dy < 0){
                result.push_back("SOUTH");
                dy += 1;
            }
            else{
                result.push_back("NORTH");
                dy -= 1;
            }
        }
        return result;
    }
};

int main(){
    DirReduction d = DirReduction();
    vector<string> dirs = {"NORTH","SOUTH","SOUTH","EAST","WEST","NORTH", "NORTH"};
    vector<string> total_dir = d.dirReduc(dirs);
    for (string dir: total_dir) cout << dir << " ";
    return 0;
}
// class DirReduction
// {
// public:
//     static string to_lower(string direction){
//         string result = direction;
//         for (char& c: result) c = tolower(c);
//         return result;
//     }
//     static string inverse_direction(string direction){
//         if (to_lower(direction) == "north") return "south";
//         else if (to_lower(direction) == "south") return "north";
//         else if (to_lower(direction) == "east") return "west";
//         else if (to_lower(direction) == "west") return "east";
//         else return "";

//     }
//     static vector<string> dirReduc(vector<string> &arr){
//         deque<string> modified_dir;
//         vector<string> result;
//         deque<string> directions;
//         for (string direction: arr) directions.push_back(direction);
//         while (!directions.empty()){
//             if (modified_dir.size() == 0){
//                 modified_dir.push_front(directions.front());
//                 directions.pop_front();
//             }
//             else if (modified_dir.front() == inverse_direction(directions.front())) directions.pop_front();
//             else{
//                 result.push_back(directions.front());
//                 directions.pop_front();
//             }
//         }
//         for (string direction: modified_dir) result.push_back(direction);
//         return result;
        
//     }
// };





// north south west west
// deque the same
// 

// string to_lower(string direction){
//         string result = direction;
//         for (char& c: result) c = tolower(c);
//         return result;
//     }
// int main(){
//     string direction = "NorTh";
//     string low_direction = to_lower(direction);
//     cout << low_direction;
//     return 0;
// }