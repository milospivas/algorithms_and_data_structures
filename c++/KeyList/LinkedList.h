/**
    LinkedList.cpp
    Purpose: Singly-linked list declaration.

    @author Miloš Pivaš
    @version 0.0.1 02/20
*/

#pragma once
#include <iostream>

/** Simple node struct to be used to form lists.
 */
template <typename T>
struct Node {
    T data;
    Node *next;

    Node(T);
};

/** Singly-linked list class.
 * 
 * Uses Node<T> class for list elements.
 * Elements can be added at both head and tail side, but only popped from the head side.
 */
template <typename T>
class LinkedList {
public:
    LinkedList();
    ~LinkedList();

    void add_head(T x);   // stack.push()
    void add_tail(T x);   // queue.enqueue()
    T pop_head();         // stack.pop() i.e. queue.dequeue()
    // T pop_tail(); // this can't be done with singly-linked lists (in O(1) time)
    bool is_empty();
    size_t len();
protected:
    Node<T>*head;
    Node<T>*tail;
    size_t _len_;
};

#include "LinkedList.tcc"
