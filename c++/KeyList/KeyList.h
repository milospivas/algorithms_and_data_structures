#include "LinkedList.h"
#include <iostream>
// #include <cstdlib>
// #include <cmath>
// #include <climits>
// #include <random>
// #define INITIAL_TABLE_SIZE 16


/** A simple key-value pair struct.
 * 
 * Used for storing keys and values in the hash table.
 */
template <typename K, typename V>
struct KVpair {
public:
    K key;
    V value;
    KVpair() = default;
    KVpair(K, V);

    /** Prints the key and value of the given KVpair.
     */
    friend std::ostream& operator<<(std::ostream& os, const KVpair & p)  {
        os << "Key: " << p.key << " Value: " << p.value;
        return os;
    }
};

/** Key-value pair constructor.
 */
template <typename K, typename V>
KVpair<K, V>::KVpair(K x, V y) {
    key = x;
    value = y;
}


/** Linked list for storing the key-value pairs in the hash table.
 * 
 * Inherits LinkedList.
 */
template <typename K, typename V>
class KeyList : public LinkedList<KVpair<K, V>> {
public:
    bool find(K);    // TODO implement
    V get(K);        // TODO implement
    void set(K, V);  // TODO implement
    V remove(K);
};