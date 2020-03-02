#include "InsertionSort.h"

void InsertionSort::swap(std::vector<int> &a, int i, int j) {
    if (i == j) {
        return;
    }    
    int aux = a[i];
    a[i] = a[j];
    a[j] = aux;
    return;
}
void InsertionSort::sort(std::vector<int> &a, int start, int end) {
    for (int i = start + 1; i < end; i++) {
        for (int j = i; (j > 0) && (a[j-1] > a[j]); j--) {
            InsertionSort::swap(a, j, j-1);
        }
    }
}

int main() {
    std::vector<int> A{9, 8, 7, 6, 5, 4, 3, 2, 1, 0}; //{42, 3, 8, 2, 5, 1, 4, 7, 6}; //3, 1, 2, 6, 4, 7};
    int n = A.size();
    InsertionSort::sort(A, 0, n);
    
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
    
    return sol;
}