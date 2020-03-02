#pragma once
#include <vector>
#include <random>

namespace QuickSort {
    std::vector<int> swap(std::vector<int> &a, int i, int j);
    int get_pivot(std::mt19937 gen, int start, int end);
    int partition(std::vector<int> &a, int start, int end, int p);
    std::vector<int> quicksort_rec(std::vector<int> &a, int start, int end, std::mt19937 gen);
    std::vector<int> sort(std::vector<int> &a);
};