#include "KeyList.h"

/** Key-value pair constructor.
 */
template <typename K, typename V>
KVpair<K, V>::KVpair(K x, V y) {
    key = x;
    val = y;
    // std::cout << "KVpair constructor called" << std::endl;
}

template <typename K, typename V>
bool KeyList<K, V>::find(K key) {
    Node<KVpair<K,V>>* aux = this->head;
    while (nullptr != aux) {
        if (key == aux->data.key) {
            return true;
        }
        aux = aux->next;
    }
    return false;
}

template <typename K, typename V>
V KeyList<K, V>::get(K key) {
    Node<KVpair<K,V>>* aux = this->head;
    while (nullptr != aux) {
        if (key == aux->data.key) {
            return aux->data.val;
        }
        aux = aux->next;
    }
    throw std::logic_error("KeyError. Key not in list.");
}

template <typename K, typename V>
void KeyList<K, V>::set(K key, V val) {
    Node<KVpair<K,V>>* aux = this->head;
    while (nullptr != aux) {
        if (key == aux->data.key) {
            aux->data.val = val;
            return;
        }
        aux = aux->next;
    }
    // if key not found, add it to the list
    this->add_head(KVpair<K, V>(key, val));
}

template <typename K, typename V>
V KeyList<K, V>::remove(K key) {
    // if the key is on the begining of the list, just pop_head
    if (key == this->head->data.key) {
        return this->pop_head().val;    // pop the KVpair
    }
    // else, if the key is deeper in the list
    // start from the head
    Node<KVpair<K,V>>* aux = this->head;
    // always look at the next Node from the current
    while (nullptr != aux->next) {
        if (key == aux->next->data.key) {
            Node<KVpair<K,V>>* old = aux->next; // take the old Node
            V val = old->data.val;          // save the val

            aux->next = aux->next->next;        // reconnect the next of the current node to the second next
            
            if (old == this->tail) {            // if the key is at the tail of the list
                this->tail = aux;               // the current element becomes the tail
            }
            this->_len_--;

            // delete kvp;
            delete old;

            return val;
        }
        aux = aux->next;
    }
    throw std::logic_error("KeyError. Key not in list.");    
}


// // For testing
// int main() {
//     KeyList<int, int> kl;
    
//     try {
//         std::cout << "Finding key=42..." << std::endl;
//         bool flag = kl.find(42);
//         std::cout << flag << std::endl;
//     }
//     catch(std::logic_error e) {
//         std::cout << e.what() << std::endl;
//     }

//     try {
//         std::cout << "Getting key=42..." << std::endl;
//         int val = kl.get(42);
//         std::cout << val << std::endl;
//     }
//     catch(std::logic_error e) {
//         std::cout << e.what() << std::endl;
//     }

//     try {
//         std::cout << "Setting key=42, to 73..." << std::endl;
//         kl.set(42, 73);
//         std::cout << "Set!" << std::endl;
//     }
//     catch(std::logic_error e) {
//         std::cout << e.what() << std::endl;
//     }

//     try {
//         std::cout << "Finding key=42..." << std::endl;
//         bool flag = kl.find(42);
//         std::cout << flag << std::endl;
//     }
//     catch(std::logic_error e) {
//         std::cout << e.what() << std::endl;
//     }

//     try {
//         std::cout << "Getting key=42..." << std::endl;
//         int val = kl.get(42);
//         std::cout << "Value is: " <<val << std::endl;
//     }
//     catch(std::logic_error e) {
//         std::cout << e.what() << std::endl;
//     }

//     try {
//         std::cout << "Removing key=42..." << std::endl;
//         int val = kl.remove(42);
//         std::cout << "Value is: " <<val << std::endl;
//     }
//     catch(std::logic_error e) {
//         std::cout << e.what() << std::endl;
//     }



//     std::cout << "Test 42,1,2" << std::endl;
//     kl.set(42, 42);
//     kl.set(1, 1);
//     kl.set(2, 2);
//     kl.remove(42);

//     while (not kl.is_empty()) {
//         int val = kl.pop_head().val;
//         std::cout << val << std::endl;
//     }

//     std::cout << "Test 1,42,2" << std::endl;
//     kl.set(1, 1);
//     kl.set(42, 42);
//     kl.set(2, 2);
//     kl.remove(42);

//     while (not kl.is_empty()) {
//         int val = kl.pop_head().val;
//         std::cout << val << std::endl;
//     }

    
//     std::cout << "Test 1,2,42" << std::endl;
//     kl.set(1, 1);
//     kl.set(2, 2);
//     kl.set(42, 42);
//     kl.remove(42);

//     while (not kl.is_empty()) {
//         int val = kl.pop_head().val;
//         std::cout << val << std::endl;
//     }

//     std::cout << "Test 1,2" << std::endl;
//     kl.set(1, 1);
//     kl.set(2, 2);
//     kl.remove(42);

//     while (not kl.is_empty()) {
//         int val = kl.pop_head().val;
//         std::cout << val << std::endl;
//     }

//     return 0;
// }