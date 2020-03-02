/**
    LinkedList.tcc
    Purpose: Singly-linked list class template implementation.

    @author Miloš Pivaš
    @version 0.0.1 02/20
*/

#include "LinkedList.h"

/** List node constructor.
 */
template <typename T>
Node<T>::Node(T x) {
    data = x;
    next = nullptr;
}

/** List constructor.
 */
template <typename T>
LinkedList<T>::LinkedList() {
    head = tail = nullptr;
    _len_ = 0;
}

/** List destructor.
 */
template <typename T>
LinkedList<T>::~LinkedList() {
    while(nullptr != head) {
        Node<T>* old = head;
        head = head->next;
        // delte old->data;
        delete old;        
    }
}

/** Appends a node to the head of the list.
 * 
 * Similar to stack.push().
 * @param x data to be appended inside the node.
 */
template <typename T>
void LinkedList<T>::add_head(T x) {
    Node<T> *new_node = new Node<T>(x);
    _len_++;

    if (nullptr == head) {
        head = tail = new_node;
    }
    else {
        new_node->next = head;
        head = new_node;
    }
}

/** Appends a node to the tail of the list.
 * 
 * Similar to queue.enqueue().
 * @param x data to be appended inside the node.
 */
template <typename T>
void LinkedList<T>::add_tail(T x) {
    Node<T> *new_node = new Node<T>(x);
    _len_++;

    if (nullptr == tail) {
        head = tail = new_node;
    }
    else {
        tail->next = new_node;
        tail = new_node;
    }
}

/** Remove a node from the head of the list.
 * 
 * Similar to stack.pop() or queue.dequeue().
 * @return the data from inside the removed head of the list.
 */
template <typename T>
T LinkedList<T>::pop_head() {
    if (_len_ > 0) {
        T data = head->data;
        Node<T>* old = head;
        head = head->next;
        _len_--;
        if (0 == _len_) {
            tail = nullptr;
        }
        delete old;
        return data;
    }
    else {
        throw std::logic_error("Error. Popping from an empty list.");
    }
}

/** Check if the list is empty.
 * 
 * @return true if the list is empty, otherwise false.
 */
template <typename T>
bool LinkedList<T>::is_empty() {
    if (nullptr == head) {
        return true;
    }
    else {
        return false;
    }
}

/** Get the length of the list.
 * 
 * @return the length of the list.
 */
template <typename T>
size_t LinkedList<T>::len() {
    return _len_;
}
