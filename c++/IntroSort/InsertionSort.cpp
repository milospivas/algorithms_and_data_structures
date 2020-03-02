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