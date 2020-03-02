#include "IntroSort.h"
#include <iostream>

std::vector<int> IntroSort::swap(std::vector<int> &a, int i, int j) {
    if (i == j) {
        return a;
    }
    int aux = a[i];
    a[i] = a[j];
    a[j] = aux;
    return a;
}

int IntroSort::get_pivot(std::mt19937 gen, int start, int end) {
    std::uniform_int_distribution<> dis(start, end-1);
    return dis(gen);
}

int IntroSort::partition(std::vector<int> &a, int start, int end, int p) {
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

std::vector<int> IntroSort::quicksort_rec(std::vector<int> &a, int start, int end, int depth_limit, std::mt19937 gen) {
    int n = end - start;
    if (n <= 1) {
        return a;
    }
    else if (n <= 16) {
        InsertionSort::sort(a, start, end);
    }
    else if (depth_limit <= 0) {
        MaxHeap::sort(a, start, end);
        return a;
    }
    else {
        int p = start; //get_pivot(gen, start, end);
        p = partition(a, start, end, p);

        quicksort_rec(a, start, p, depth_limit - 1, gen);
        quicksort_rec(a, p+1, end, depth_limit - 1, gen);
        return a;
    }
    return a;
}

std::vector<int> IntroSort::sort(std::vector<int> &a, int start, int end) {
    int n = end - start;
    std::random_device rd;  //Will be used to obtain a seed for the random number engine
    std::mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
    int depth_limit = (int)2*log(n);
    quicksort_rec(a, start, end, depth_limit, gen);
    return a;
}

int main() {
    std::vector<int> A{9, 8, 7, 6, 5, 4, 3, 2, 1, 0}; //{42, 3, 8, 2, 5, 1, 4, 7, 6}; //3, 1, 2, 6, 4, 7};
    int n = A.size();
    IntroSort::sort(A, 0, n);
    
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