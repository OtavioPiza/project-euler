#include <stdlib.h>
#include <stdio.h>

// == Project Euler: Problem 1 ================================================================== //
/**
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
 */

// == Solution ================================================================================== //

int  main(int argc, char **argv) {
    int upperbound = argc >= 1 ? atoi(argv[1]) : 1000;
    int result = 0;

    for (int i = 3; i < upperbound; i += 2) {
        if (i % 3 == 0 || i % 5 == 0) {
            result++;
        }
    }
    printf("The answer is: %d\n", result);
    return 0;
}