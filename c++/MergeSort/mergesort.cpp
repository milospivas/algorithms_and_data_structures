#include <vector>
#include <iostream>

using namespace std;

vector<int> merge(vector<int> &a, vector<int> &b, int start, int mid, int end) {
    int n = end - start;
    int j = start;
    int k = mid;
    for (int i = 0; i < n; i++) {
        if ((k == end) || ((j < mid) && (a[j] < a[k]))) {
            b[i] = a[j];
            j++;
        }
        else {
            b[i] = a[k];
            k++;
        }
    }
    for (int i = 0; i < n; i++) {
        a[start + i] = b[i];    
    }
    return a;
}

vector<int> mergesort_rec(vector<int> &a, vector<int> &b, int start, int end) {
    int n = end - start;
    
    if (n <= 1) {
        return a;
    }
    if (2 == n) {
        if (a[start] > a[start + 1]) {
            int aux = a[start];
            a[start] = a[start + 1];
            a[start + 1] = aux;
        }
        return a;
    }
    
    int mid = start + n/2;
    mergesort_rec(a, b, start, mid);
    mergesort_rec(a, b, mid, end);
    merge(a, b, start, mid, end);
    return a;
}

vector<int> mergesort(vector<int> &a) {
    int n = a.size();
    vector<int> b(n, 0);
    
    mergesort_rec(a, b, 0, n);
    return a;
}

int main() {
    vector<int> A{3, 1, 2, 6, 4, 7};
    int n = A.size();
    mergesort(A);
    
    int cnt = 1;
    int sol = A[n-1];
    for (int i = 1; i < n; i++) {
        if (A[i] == A[i-1]) {
            cnt++;
        }
        else {
            if ((cnt % 2) == 1) {
                sol = A[i-1];
                break;
            }
            cnt = 1;
        }
    }

    // int a[n];
    // for (int i = 0; i < n; i++) {
    //     a[i] = A[i];
    // }
    // mergesort(a);
    
    // int cnt = 1;
    // int sol = a[n-1];
    // for (int i = 1; i < n; i++) {
    //     if (a[i] == a[i-1]) {
    //         cnt++;
    //     }
    //     else {
    //         if ((cnt % 2) == 1) {
    //             sol = a[i-1];
    //             break;
    //         }
    //         cnt = 1;
    //     }
    // }
    
    
    return sol;
}