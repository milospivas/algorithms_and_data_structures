#pragma once
#include "LinkedList.h"
#include <iostream>

/** A simple key-value pair struct.
 * 
 * Used for storing keys and values in the hash table.
 */
template <typename K, typename V>
struct KVpair {
public:
    K key;
    V val;
    KVpair() = default;
    KVpair(K, V);

    /** Prints the key and value of the given KVpair.
     */
    friend std::ostream& operator<<(std::ostream& os, const KVpair & p)  {
        os << "Key: " << p.key << " Value: " << p.val;
        return os;
    }
};



/** Linked list for storing the key-value pairs in the hash table.
 * 
 * Inherits LinkedList.
 */
template <typename K, typename V>
class KeyList : public LinkedList<KVpair<K, V>> {
public:
    bool find(K);
    V get(K);
    void set(K, V);
    V remove(K);
};

#include "KeyList.tcc"