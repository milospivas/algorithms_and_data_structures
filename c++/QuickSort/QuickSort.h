#pragma once
#include <iostream>
#include <vector>
#include <random>

namespace QuickSort {
    std::vector<int> swap(std::vector<int> &a, size_t i, size_t j);
    size_t get_pivot(std::mt19937 gen, size_t start, size_t end);
    size_t partition(std::vector<int> &a, size_t start, size_t end, size_t p);
    std::vector<int> quicksort_rec(std::vector<int> &a, size_t start, size_t end, std::mt19937 gen);
    std::vector<int> sort(std::vector<int> &a);
};