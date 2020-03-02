#include "MaxHeap.h"

template <typename T>
void MaxHeap::swap(T a[], size_t i, size_t j) {
    if (i == j) {
        return;
    }    
    T aux = a[i];
    a[i] = a[j];
    a[j] = aux;
    return;
}

template <typename T>
void MaxHeap::sift_down(T a[], size_t root, size_t end, size_t i) {
    // while you are above the leaves
    while (LEFT_CHILD(root, i) < end) {
        // find the larger child
        size_t larger = LEFT_CHILD(root, i); //2*i + 1;
        if ((larger + 1 < end) && (a[larger + 1] > a[larger])) {
            larger++;
        }
        // if there's a max-heap violation, sift down
        if (a[i] < a[larger]) {
            MaxHeap::swap<T>(a, i, larger);
            i = larger;
        }
        else {
            break;
        }
    }
    return;
}

template <typename T>
void MaxHeap::heapify(T a[], size_t root, size_t end) {
    // from above the leaves up to the root
    for (size_t i = LAST_PARENT(root, end); i >= root; i--) {
        MaxHeap::sift_down<T>(a, root, end, i);
        if (root == i) { // to prevent underflow if i is unsigned
            break;
        }
    }

    return;
}

template <typename T>
T MaxHeap::extract(T a[], size_t root, size_t end) {
    MaxHeap::swap<T>(a, root, end-1);
    MaxHeap::sift_down<T>(a, root, end-1, root);
    return a[end-1];
}


template <typename T>
void MaxHeap::sort(T a[], size_t root, size_t end) {
    MaxHeap::heapify<T>(a, root, end);
    for (size_t unsorted_end = end; unsorted_end > root; unsorted_end--) {
        MaxHeap::extract<T>(a, root, unsorted_end);
    }
    return;
}
