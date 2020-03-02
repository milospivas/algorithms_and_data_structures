#include "HashTable.h"

int main() {
    // testing
    size_t n = 10;
    // std::cout << sizeof(size_t) << std::endl;

    HashTable<int, int> h = HashTable<int, int>();


    // int x = 42;
    // for (size_t i = 0; i < h.size(); i++) {
    //     h.temp[i] = &x;
    //     std::cout << *(h.temp[i]) << std::endl;
    // }

    // size_t m = h.size();
    int key[n];
    size_t hash[n];

    // size_t o[m+1];
    // for (size_t i = 0; i < m+1; i++) {
    //     o[i] = 0;
    // }

    std::random_device rd;  //Will be used to obtain a seed for the random number engine
    std::mt19937 gen(rd()); //Standard mersenne_twister_engine seeded with rd()
    std::uniform_int_distribution<> dis(INT_MIN, INT_MAX);

    for (size_t i = 0; i < n; i++) {
        key[i] = dis(gen); //i;
        hash[i] = h.hash(key[i]);
        // o[hash[i]]++;
        std::cout << std::endl;
        std::cout << "Inserting the element with value: " << i << std::endl;
        h.set(key[i], i);
        std::cout << "Elements in the table: " << h.len() << std::endl;
        h.print();
    }

    std::cout << "Elements in the table: " << h.len() << std::endl;
    h.print();

    for (size_t i = 0; i < n; i++) {
        std::cout << std::endl;
        std::cout << "Changing the element with key " << key[i] << " to value: " << 100+i << std::endl;
        h.set(key[i], 100+i);
        std::cout << "Elements in the table: " << h.len() << std::endl;
        h.print();
    }

    for (size_t i = 0; i < n; i++) {
        std::cout << std::endl;
        int val = h.remove(key[i]); // TODO uncomment
        std::cout << "Removed element with value: " << val << std::endl;
        std::cout << "Elements left in the table: " << h.len() << std::endl;
        std::cout << "Size of the table: " << h.size() << std::endl;
        h.print();
    }


    // double mean = 0;
    // size_t collisions_max = 0;
    // for (size_t i = 0; i < m+1; i++) {
    //     mean += o[i];

    //     if (o[i] > collisions_max) {
    //         collisions_max = o[i];
    //     }
    //     // std::cout << i << " : " << o[i] << std::endl;
    // }
    // mean /= m + 1;

    // std::cout << "Mean number of hash value occurrences = " << mean << std::endl;
    // std::cout << "Load factor n/m = " << 1.0*n/m << std::endl;
    // std::cout << std::endl;

    // std::cout << "Max no. of collisions = " << collisions_max << std::endl;

    std::cout << std::endl;

    // std::cout << "key" << " : " << "hash" << std::endl;
        // std::cout << key[i] << " : " << hash[i] << std::endl;
    return 0;
}