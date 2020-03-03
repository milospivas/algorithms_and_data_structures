/**
    HashTable.h
    Purpose: Hash table declaration.

    @author Miloš Pivaš
    @version 0.0.1 02/20
*/

#pragma once
#include "KeyList.h"
#include <cstdlib>
#include <cmath>
#include <climits>
#include <random>
#define TABLE_SIZE_MIN 8
#define W 8 * sizeof(size_t) // hash word length in bits
#define TABLE_HALVING_PERCENT 0.25
#define TABLE_GROWTH_FACTOR 2
#define TABLE_SHRINK_FACTOR 0.5

/** Hash table class.
 * 
 * Uses universal hashing, chaining and table doubling
 */
template <typename K, typename V>
class HashTable {
public:
    unsigned short M;
    size_t hash(K x);
    size_t len();
    size_t size();
    void set(K x, V y);
    V get(K x);
    V remove(K x);

    void print();

    HashTable(size_t initial_size = TABLE_SIZE_MIN);
    ~HashTable(); // TODO implement



private:
    size_t a, b;
    size_t _size_, _len_;
    KeyList<K, V> **_h_;
    void recompute_hash_parameters();
    void rehash(KeyList<K,V>** old_table, size_t old_size);
    void _set_(K x, V y);
    V _remove_(K x);
    void table_change_size(float scaling_factor);
};

#include "HashTable.tcc"