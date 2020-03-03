/**
    HashTable.tcc
    Purpose: Hash table implementation using
    universal hashing, chaining and table doubling.

    @author Miloš Pivaš
    @version 0.0.1 02/20
*/

#include "HashTable.h"

/** Rounds to the next power of 2.
 *
 * @param x the number to be rounded.
 * @return the smallest power of 2 greater than or equal to x.
 * */
inline size_t nextpow2 (size_t x) {
    if (x < 0)
        return 0;
    --x;
    x |= x >> 1;
    x |= x >> 2;
    x |= x >> 4;
    x |= x >> 8;
    x |= x >> 16;
    x |= x >> 32;
    return x+1;
}

/** HashTable constructor 
 *
 * @param initial_size the initial allocated size of the hash table
 * */
template <typename K, typename V>
HashTable<K, V>::HashTable(size_t initial_size) {
    // calculating the hash-table parameters
    _size_ = nextpow2(initial_size);    // table size rounded to the next power of 2
    M = (unsigned short)std::ilogb(_size_); // maximum word length for the hash values in bits
    
    // generating the random a and b parameters for universal hashing
    std::random_device rd;
    std::mt19937_64 gen(rd());  //Standard mersenne_twister_engine seeded with rd()
    size_t a_limit = (size_t)(-1); //UINT_MAX; //?
    size_t b_limit = (size_t)((1 << (W - M)) - 1);
    std::uniform_int_distribution<size_t> a_distribution = std::uniform_int_distribution<size_t>(0, a_limit);  // distribution for parameter a
    std::uniform_int_distribution<size_t> b_distribution = std::uniform_int_distribution<size_t>(0, b_limit);  // distribution for parameter b
    a = b = 0;
    while ((a % 2) == 0) {
        a = a_distribution(gen);
    }
    while ((b % 2) == 0) {
        b = b_distribution(gen);
    }
    
    // initializing the array of pointers to list of key-value pairs
    // temp = new int*[_size_];
    _h_ = new KeyList<K, V>*[_size_];
    for (size_t i = 0; i < _size_; i++) {
        _h_[i] = new KeyList<K, V>();
    }
    _len_ = 0;
}

/** Hashtable destructor.
 *
 * Deletes the list from each table entry. 
 * Deletes the table.
 * */
template <typename K, typename V>
HashTable<K,V>::~HashTable() {
    for (size_t i = 0; i < _size_; i++) {
        delete _h_[i];
    }
    delete _h_;
}

/** Returns the size of the hash table.
 *
 * @return the number of elements of the hash table array.
 * */
template <typename K, typename V>
size_t HashTable<K, V>::size() {
    return this->_size_;
}

/** Returns the length of the hash table.
 *
 * @return the number of elements stored in the hash table.
 * */
template <typename K, typename V>
size_t HashTable<K, V>::len() {
    return this->_len_;
}

/** Hashes x of integer type via universal hashing.
 *
 * Uses the multiply-shift scheme described by Dietzfelbinger et al. in 1997.
 * @param x - the key to be hashed
 * @return hash - the hash valueof the key
 * */
template <typename K, typename V>
size_t HashTable<K, V>::hash(K x) {
    size_t a = this->a;
    size_t b = this->b;
    unsigned short M = this->M;
    size_t hash = (size_t) ((a*x+b) >> (W-M));
    return hash;
}


template <typename K, typename V>
void HashTable<K, V>::recompute_hash_parameters() {
    M = (unsigned short)std::ilogb(_size_); // maximum word length for the hash values in bits
    
    // generating the random a and b parameters for universal hashing
    std::random_device rd;
    std::mt19937_64 gen(rd());  //Standard mersenne_twister_engine seeded with rd()
    size_t a_limit = (size_t)(-1); //UINT_MAX; //?
    size_t b_limit = (size_t)((1 << (W - M)) - 1);
    std::uniform_int_distribution<size_t> a_distribution = std::uniform_int_distribution<size_t>(0, a_limit);    // distribution for parameter a
    std::uniform_int_distribution<size_t> b_distribution = std::uniform_int_distribution<size_t>(0, b_limit);    // distribution for parameter b
    a = b = 0;
    while ((a % 2) == 0) {
        a = a_distribution(gen);
    }
    while ((b % 2) == 0) {
        b = b_distribution(gen);
    }
}


/** Insert/change an element in the hash table.
 * 
 * @param key - the key of the inserted element
 * @param val - the value of the inserted element
 * Doesn't grow the table.
 */
template <typename K, typename V>
void HashTable<K, V>::_set_(K key, V val) {
    size_t idx = this->hash(key);
    size_t old_list_size = this->_h_[idx]->len();
    this->_h_[idx]->set(key, val);
    size_t new_list_size = this->_h_[idx]->len();
    this->_len_ += new_list_size - old_list_size;
}

/** Removes an element from the table.
 * 
 * @param key - the key of the element to be removed.
 * @return the value of the removed element.
 * Doesn't shrink the table.
 */
template <typename K, typename V>
V HashTable<K, V>::_remove_(K key) {
    if (this->_len_ == 0) {
        throw std::logic_error("Error. Removing from an empty HashTable.");
    }

    size_t idx = this->hash(key);
    V val = this->_h_[idx]->remove(key); // this should throw an exception if the key is not in the list
    this->_len_--;

    return val;
}


/** Rehash the given old_table into new table.
 * 
 * @param old_table old table to be rehashed into the current one
 * @param old_size the size of the old table
 */
template <typename K, typename V>
void HashTable<K,V>::rehash(KeyList<K,V>** old_table, size_t old_size) {
    for (size_t i = 0; i < old_size; i++) {
        while(not (old_table[i]->is_empty())) {
            KVpair<K,V> kvp = old_table[i]->pop_head();
            this->_set_(kvp.key, kvp.val);
        }
    }
}


/** Grows/shrinks the hash table by the given factor.
 *  
 * @param scaling_factor - the scaling factor by which to grow/shrink the table
 */
template <typename K, typename V>
void HashTable<K, V>::table_change_size(float scaling_factor) {
    // change the size
    size_t old_size = _size_;
    _size_ = (size_t) (_size_*scaling_factor);
    
    // save the old table, allocate the new table
    KeyList<K, V> **old_table = _h_;
    _h_ = new KeyList<K, V>*[_size_];
    for (size_t i = 0; i < _size_; i++) {
        _h_[i] = new KeyList<K, V>();
    }
    this->_len_ = 0;

    this->recompute_hash_parameters(); // self-explanatory

    // rehash
    this->rehash(old_table, old_size);

    // delete the old table
    for (size_t i = 0; i < old_size; i++) {
        delete old_table[i];
    }
    delete old_table;
}


/** Insert/change an element in the hash table.
 * 
 * @param key - the key of the inserted element
 * @param val - the value of the inserted element
 * Grows the table by the defined TABLE_GROWTH_FACTOR
 * if the number of elements in the table is equal
 * or greater than the table size.
 */
template <typename K, typename V>
void HashTable<K, V>::set(K key, V val) {
    if (this->_len_ >= this->_size_) {
        // std::cout << "Table scaling by " << TABLE_GROWTH_FACTOR << " ..." << std::endl;
        this->table_change_size(TABLE_GROWTH_FACTOR);
    }

    this->_set_(key, val);
}

/** Removes an element from the table.
 * 
 * @param key - the key of the element to be removed.
 * @return the value of the removed element.
 * Shrinks the table by the defined TABLE_SHRINK_FACTOR
 * if the number of elements in the table less than
 * the given percentage of the table size.
 */
template <typename K, typename V>
V HashTable<K, V>::remove(K key) {
    V val = this->_remove_(key);

    if ((TABLE_SIZE_MIN <= _size_ * TABLE_SHRINK_FACTOR) and (this->_len_ <= TABLE_HALVING_PERCENT*this->_size_)) {
        // std::cout << "Table scaling by " << TABLE_SHRINK_FACTOR << " ..." << std::endl;
        this->table_change_size(TABLE_SHRINK_FACTOR);
    }
    return val;
}


/** Gets an element from the table.
 * 
 * @param key - the key of the element to be retrieved.
 * @return the value of the element.
 */
template <typename K, typename V>
V HashTable<K, V>::get(K key) {
    if (this->_len_ == 0) {
        throw std::logic_error("Error. Getting from an empty HashTable");
    }

    size_t idx = this->hash(key);
    V val = this->_h_[idx]->get(key);

    return val;
}


/** Prints all elements stored in the table.
 */
template <typename K, typename V>
void HashTable<K, V>::print() {
    for (size_t i = 0; i < _size_; i++) {
        _h_[i]->print();
    }
}