#include "MinHeap.h"
#include "MaxHeap.h"

struct Pair {
    int key;
    int value;

    Pair() = default;
    Pair(int x, int y) {
        key = x;
        value = y;
    }

    friend bool operator<(const Pair& l, const Pair& r){
        return l.key < r.key;
    }
    
    friend bool operator>(const Pair& l, const Pair& r){
        return r.key < l.key;
    }
};


int main() {
    // int a[] = {42, 3, 8, 2, 5, 1, 4, 7, 6, 3, 8, 2, 5, 1, 4, 7, 6};
    // int n = 17;
    int a[] = {2, -1, 3, -1, 4, 0};
    int n = 6;
    
    Pair p(42, 42);
    Pair q(73, 73);

    bool flag = p < q;
    bool flag2 = p > q;
    std::cout << flag << std::endl;
    std::cout << flag2 << std::endl;


    MaxHeap::sort<int>(a, 0, n);
    std::cout << std::endl;
    MinHeap::sort<int>(a, 0, n);
    
    // for (int i = 0; i < n; i++) {
    //     std::cout << a[i] << " ";
    // }
    // std::cout << std::endl;

    int cnt = 1;
    int sol = a[n-1];
    for (int i = 1; i < n; i++) {
        if (a[i] == a[i-1]) {
            cnt++;
        }
        else {
            if ((cnt % 2) == 1) {
                sol = a[i-1];
                break;
            }
            cnt = 1;
        }
    }
    
    std::cout << sol << std::endl;
    
    return sol;
}