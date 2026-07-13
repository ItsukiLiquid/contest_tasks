#include <iostream>
#include <queue>
using namespace std;

class MyStack {
public:
    MyStack() {}
    queue<int> q1; // 1 2 3 4 5
    queue<int> q2; // 
    void reverse_queue(queue<int> &q1, queue<int> &q2){
        while (!q1.empty()){
            q2.push(q1.back());
            q1.pop();
        }
    }
    void push(int x) {
        q1.push(x);
    }
    
    int pop() {
        // pops last element from q1, so we need to move elements to q2 remembering last element
        int last_val = q1.back();
        for (int i = 0; i < q1.size() - 1; ++i){
            int cur_val = q1.front();
            q1.pop();
            q1.push(cur_val);
        }
        q1.pop();
        return last_val;
    }
    
    int top() {
        return q1.back();
    }
    
    bool empty() {
        return q1.empty();
    }
    void show(){
        while (!q1.empty()){
            cout << q1.front() << " ";
            q1.pop();
        }
        cout << endl;
    }
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack* obj = new MyStack();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->top();
 * bool param_4 = obj->empty();
 */

int main() {
    MyStack* obj = new MyStack();
    while (true) {
        int choice;
        cout << "Enter your choice (1: push, 2: pop, 3: top, 4: empty, 5: exit): ";
        cin >> choice;
        if (choice == 1) {
            int x;
            cout << "Enter value to push: ";
            cin >> x;
            obj->push(x);
        } else if (choice == 2) {
            cout << "Popped value: " << obj->pop() << endl;
        } else if (choice == 3) {
            cout << "Top value: " << obj->top() << endl;
        } else if (choice == 4) {
            cout << "Is stack empty? " << (obj->empty() ? "Yes" : "No") << endl;
        } else if (choice == 6) obj->show();
        else if (choice == 5) {
            break;
        } else {
            cout << "Invalid choice. Please try again." << endl;
        }
    }
    return 0;
}