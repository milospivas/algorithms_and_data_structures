#pragma once

#include <vector>
#define LEFT_CHILD(root, i) root + 2*(i - root) + 1
#define FIRST_LEAF(root, end) root + (end - root)/2
#define LAST_PARENT(root, end) FIRST_LEAF(root, end) - 1

namespace MinHeap {
    void swap(std::vector<int> &a, int i, int j);
    void sift_down(std::vector<int> &a, int root, int end, int i);
    // void sift_up(std::vector<int> &a, int root, int end, int i);
    void heapify(std::vector<int> &a, int root, int end);
    int extract(std::vector<int> &a, int root, int end);
    void sort(std::vector<int> &a, int root, int end);
};