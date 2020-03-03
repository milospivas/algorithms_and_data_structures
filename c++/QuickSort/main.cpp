#include "QuickSort.h"

int main() {
    std::vector<int> A{3, 8, 2, 5, 1, 4, 7, 6}; //3, 1, 2, 6, 4, 7};
    size_t n = A.size();

    for (size_t i = 0; i < n; i++) {
        std::cout << A[i] << " ";
    }
    std::cout << std::endl;

    QuickSort::sort(A);
    
    for (size_t i = 0; i < n; i++) {
        std::cout << A[i] << " ";
    }
    std::cout << std::endl;
    return 0;
}