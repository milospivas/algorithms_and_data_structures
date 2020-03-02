#include "main.h"

Pair::Pair(int x, int y) {
    first = x;
    second = y;
}

int main() {
    LinkedList<Pair> l;

    l.add_head(Pair(42, 73));

    Pair p = l.pop_head();
    std::cout << p.first << " " << p.second << std::endl;
    std::cout << std::endl;
    return 0;
}