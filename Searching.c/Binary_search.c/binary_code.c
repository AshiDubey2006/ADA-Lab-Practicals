#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Binary Search Function
int binarySearch(int arr[], int n, int x) {
    int low = 0, high = n - 1, mid;
    while (low <= high) {
        mid = (low + high) / 2;
        if (arr[mid] == x)
            return mid;
        else if (arr[mid] < x)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

int main() {
    int n, *arr, x, i, result, dummy = 0;
    clock_t start, end;
    double time_taken;
    int REPEAT = 1000000;    // searches per run
    int RUNS = 5;            // number of runs to average

    printf("Binary Search Time Analysis\n");

    for (n = 10000; n <= 100000; n += 10000) {
        arr = (int *)malloc(n * sizeof(int));

        // Fill array with sorted numbers
        for (i = 0; i < n; i++)
            arr[i] = i + 1;

        x = n; // search for last element

        double total_time = 0.0;

        // Average multiple runs to smooth fluctuations
        for (int run = 0; run < RUNS; run++) {
            start = clock();
            for (int r = 0; r < REPEAT; r++) {
                result = binarySearch(arr, n, x);
                dummy += result;  // prevent optimization
            }
            end = clock();
            total_time += ((double)(end - start)) / CLOCKS_PER_SEC;
        }

        time_taken = total_time / (RUNS*1000)
        
        ;  // average time
        printf("n = %d, Time taken = %f seconds (averaged over %d runs)\n", n, time_taken, RUNS);

        free(arr);
    }

    // Use dummy to avoid optimization
    printf("Ignore this: %d\n", dummy);

    return 0;
}
