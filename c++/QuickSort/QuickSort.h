#pragma once
#include <iostream>
#include <vector>
#include <random>

namespace QuickSort {
    template <typename T>
    std::vector<T> swap(std::vector<T> &a, size_t i, size_t j);
    
    size_t get_pivot(std::mt19937 gen, size_t start, size_t end);
    
    template <typename T>
    size_t partition(std::vector<T> &a, size_t start, size_t end, size_t p);
    
    template <typename T>
    std::vector<T> quicksort_rec(std::vector<T> &a, size_t start, size_t end, std::mt19937 gen);
    
    template <typename T>
    std::vector<T> sort(std::vector<T> &a);
};

#include "QuickSort.tcc"