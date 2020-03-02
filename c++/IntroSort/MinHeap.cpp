#include "MinHeap.h"
#include <iostream>

void MinHeap::swap(std::vector<int> &a, int i, int j) {
    if (i == j) {
        return;
    }    
    int aux = a[i];
    a[i] = a[j];
    a[j] = aux;
    return;
}

void MinHeap::sift_down(std::vector<int> &a, int root, int end, int i) {
    // while you are above the leaves
    while (LEFT_CHILD(root, i) < end) {
        // find the smaller child
        int smaller = LEFT_CHILD(root, i); //2*i + 1;
        if ((smaller + 1 < end) && (a[smaller + 1] < a[smaller])) {
            smaller++;
        }
        // if there's a min-heap violation, sift down
        if (a[i] > a[smaller]) {
            MinHeap::swap(a, i, smaller);
            i = smaller;
        }
        else {
            break;
        }
    }
    return;
}

void MinHeap::heapify(std::vector<int> &a, int root, int end) {
    // from above the leaves up to the root
    for (int i = LAST_PARENT(root, end); i >= root; i--) {
        MinHeap::sift_down(a, root, end, i);
    }
    return;
}

int MinHeap::extract(std::vector<int> &a, int root, int end) {
    MinHeap::swap(a, root, end-1);
    MinHeap::sift_down(a, root, end-1, root);
    return a[end-1];
}


void MinHeap::sort(std::vector<int> &a, int root, int end) {
    MinHeap::heapify(a, root, end);
    for (int unsorted_end = end; unsorted_end > root; unsorted_end--) {
        MinHeap::extract(a, root, unsorted_end);
    }
    return;
}

// int main() {
//     std::vector<int> A{42, 3, 8, 2, 5, 1, 4, 7, 6, 3, 8, 2, 5, 1, 4, 7, 6};
//     int n = A.size();
    
//     MinHeap::sort(A, 0, n);
    
//     // for (int i = 0; i < n; i++) {
//     //     std::cout << A[i] << " ";
//     // }
//     // std::cout << std::endl;

//     int cnt = 1;
//     int sol = A[n-1];
//     for (int i = 1; i < n; i++) {
//         if (A[i] == A[i-1]) {
//             cnt++;
//         }
//         else {
//             if ((cnt % 2) == 1) {
//                 sol = A[i-1];
//                 break;
//             }
//             cnt = 1;
//         }
//     }
    
//     std::cout << sol << std::endl;
    
//     return sol;
// }