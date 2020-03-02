#pragma once
#include <iostream>

#define LEFT_CHILD(root, i) root + 2*(i - root) + 1
#define FIRST_LEAF(root, end) root + (end - root)/2
#define LAST_PARENT(root, end) FIRST_LEAF(root, end) - 1

namespace MinHeap {
    template <typename T>
    void swap(T a[], size_t i, size_t j);
    
    template <typename T>
    void sift_down(T a[], size_t root, size_t end, size_t i);
    
    // template <typename T>
    // void sift_up(T a[], size_t root, size_t end, size_t i);
    
    template <typename T>
    void heapify(T a[], size_t root, size_t end);
    
    template <typename T>
    T extract(T a[], size_t root, size_t end);
    
    template <typename T>
    void sort(T a[], size_t root, size_t end);
};

#include "MinHeap.tcc"