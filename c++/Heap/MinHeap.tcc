#include "MinHeap.h"

template <typename T>
void MinHeap::swap(T a[], size_t i, size_t j) {
    if (i == j) {
        return;
    }    
    T aux = a[i];
    a[i] = a[j];
    a[j] = aux;
    return;
}

template <typename T>
void MinHeap::sift_down(T a[], size_t root, size_t end, size_t i) {
    // while you are above the leaves
    while (LEFT_CHILD(root, i) < end) {
        // find the smaller child
        size_t smaller = LEFT_CHILD(root, i); //2*i + 1;
        if ((smaller + 1 < end) && (a[smaller + 1] < a[smaller])) {
            smaller++;
        }
        // if there's a max-heap violation, sift down
        if (a[i] > a[smaller]) {
            MinHeap::swap<T>(a, i, smaller);
            i = smaller;
        }
        else {
            break;
        }
    }
    return;
}

template <typename T>
void MinHeap::heapify(T a[], size_t root, size_t end) {
    // from above the leaves up to the root
    for (size_t i = LAST_PARENT(root, end); i >= root; i--) {
        MinHeap::sift_down<T>(a, root, end, i);
        if (root == i) { // to prevent underflow if i is unsigned
            break;
        }
    }

    return;
}

template <typename T>
T MinHeap::extract(T a[], size_t root, size_t end) {
    MinHeap::swap<T>(a, root, end-1);
    MinHeap::sift_down<T>(a, root, end-1, root);
    return a[end-1];
}


template <typename T>
void MinHeap::sort(T a[], size_t root, size_t end) {
    MinHeap::heapify<T>(a, root, end);
    for (size_t unsorted_end = end; unsorted_end > root; unsorted_end--) {
        MinHeap::extract<T>(a, root, unsorted_end);
    }
    return;
}
