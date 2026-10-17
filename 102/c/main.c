#include <stdlib.h>

#include "deque.h"

int main() {
    Deque* q = new_deque();
    free(q);
    return 0;
}