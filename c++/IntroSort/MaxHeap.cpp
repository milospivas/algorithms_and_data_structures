#include "MaxHeap.h"

void MaxHeap::swap(std::vector<int> &a, int i, int j) {
    if (i == j) {
        return;
    }    
    int aux = a[i];
    a[i] = a[j];
    a[j] = aux;
    return;
}

void MaxHeap::sift_down(std::vector<int> &a, int root, int end, int i) {
    // while you are above the leaves
    while (LEFT_CHILD(root, i) < end) {
        // find the larger child
        int larger = LEFT_CHILD(root, i); //2*i + 1;
        if ((larger + 1 < end) && (a[larger + 1] > a[larger])) {
            larger++;
        }
        // if there's a max-heap violation, sift down
        if (a[i] < a[larger]) {
            MaxHeap::swap(a, i, larger);
            i = larger;
        }
        else {
            break;
        }
    }
    return;
}

void MaxHeap::heapify(std::vector<int> &a, int root, int end) {
    // from above the leaves up to the root
    for (int i = LAST_PARENT(root, end); i >= root; i--) {
        MaxHeap::sift_down(a, root, end, i);
    }
    return;
}

int MaxHeap::extract(std::vector<int> &a, int root, int end) {
    MaxHeap::swap(a, root, end-1);
    MaxHeap::sift_down(a, root, end-1, root);
    return a[end-1];
}


void MaxHeap::sort(std::vector<int> &a, int root, int end) {
    MaxHeap::heapify(a, root, end);
    for (int unsorted_end = end; unsorted_end > root; unsorted_end--) {
        MaxHeap::extract(a, root, unsorted_end);
    }
    return;
}