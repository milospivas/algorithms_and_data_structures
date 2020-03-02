#include "QuickSort.h"
#include <iostream>

std::vector<int> QuickSort::swap(std::vector<int> &a, int i, int j) {
    if (i == j) {
        return a;
    }
    int aux = a[i];
    a[i] = a[j];
    a[j] = aux;
    return a;
}

int QuickSort::get_pivot(std::mt19937 gen, int start, int end) {
    std::uniform_int_distribution<> dis(start, end-1);
    return dis(gen);
}

int QuickSort::partition(std::vector<int> &a, int start, int end, int p) {
    swap(a, start, p);
    int i = start;
    for (int j = start+1; j < end; j++) {
        if (a[j] < a[start]) {
            swap(a, j, i+1);
            i++;
        }
    }
    swap(a, start, i);
    return i;
}

std::vector<int> QuickSort::quicksort_rec(std::vector<int> &a, int start, int end, std::mt19937 gen) {
    int n = end - start;
    if (n <= 1) {
        return a;
    }
    int p = get_pivot(gen, start, end);
    p = partition(a, start, end, p);

    quicksort_rec(a, start, p, gen);
    quicksort_rec(a, p+1, end, gen);
    return a;
}

std::vector<int> QuickSort::sort(std::vector<int> &a) {
    int n = a.size();
    std::random_device rd;  //Will be used to obtain a seed for the random number engine
    std::mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
    quicksort_rec(a, 0, n, gen);
    return a;
}

int main() {
    std::vector<int> A{3, 8, 2, 5, 1, 4, 7, 6}; //3, 1, 2, 6, 4, 7};
    QuickSort::sort(A);
    
    int n = A.size();
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