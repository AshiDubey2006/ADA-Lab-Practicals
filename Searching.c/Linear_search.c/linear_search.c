#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Linear search function
int linearSearch(int arr[], int n, int key) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == key)
            return i;
    }
    return -1;
}

int main() {
    int maxN = 10000;      // maximum n to test
    int step = 1000;       // increment size
    int repeats = 100000;   // more repeats for smoother timings

    srand(time(0));
    printf("n,time(seconds)\n");

    for (int n = step; n <= maxN; n += step) {
        int *arr = (int*)malloc(n * sizeof(int));

        // Fill array with random numbers
        for (int i = 0; i < n; i++) {
            arr[i] = rand() % 100000;
        }

        // Force worst-case: pick last element
        int key = arr[n-1];

        clock_t start, end;
        double cpu_time;

        start = clock();
        for (int i = 0; i < repeats; i++) {
            linearSearch(arr, n, key);
        }
        end = clock();

        cpu_time = ((double)(end - start)) / CLOCKS_PER_SEC / repeats;

        printf("%d,%f\n", n, cpu_time);

        free(arr);
    }

    return 0;
}
