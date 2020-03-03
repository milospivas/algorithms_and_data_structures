/**
    QuickSort.tcc
    Purpose: QuickSort implementation with random pivot selection

    @author Miloš Pivaš
    @version 0.0.1 03/20
*/

#include "QuickSort.h"

template <typename T>
std::vector<T> QuickSort::swap(std::vector<T> &a, size_t i, size_t j) {
    if (i == j) {
        return a;
    }
    int aux = a[i];
    a[i] = a[j];
    a[j] = aux;
    return a;
}

size_t QuickSort::get_pivot(std::mt19937 gen, size_t start, size_t end) {
    std::uniform_int_distribution<> dis(start, end-1);
    return dis(gen);
}

template <typename T>
size_t QuickSort::partition(std::vector<T> &a, size_t start, size_t end, size_t p) {
    swap(a, start, p);
    size_t i = start;
    for (size_t j = start+1; j < end; j++) {
        if (a[j] < a[start]) {
            swap(a, j, i+1);
            i++;
        }
    }
    swap(a, start, i);
    return i;
}

template <typename T>
std::vector<T> QuickSort::quicksort_rec(std::vector<T> &a, size_t start, size_t end, std::mt19937 gen) {
    size_t n = end - start; // TODO Maybe check if n < 0
    if (n <= 1) {
        return a;
    }
    size_t p = get_pivot(gen, start, end);
    p = partition(a, start, end, p);

    quicksort_rec(a, start, p, gen);
    quicksort_rec(a, p+1, end, gen);
    return a;
}

template <typename T>
std::vector<T> QuickSort::sort(std::vector<T> &a) {
    size_t n = a.size();
    std::random_device rd;  //Will be used to obtain a seed for the random number engine
    std::mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
    quicksort_rec(a, 0, n, gen);
    return a;
}