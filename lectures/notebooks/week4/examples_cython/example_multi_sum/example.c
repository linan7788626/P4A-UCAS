#include "example.h"
int multi_sum_c(int a) {
    int i;
    int b = 0;
    for (i = 0; i < 10000; ++i) {
        b += a * i;
    }
    return b;
}
