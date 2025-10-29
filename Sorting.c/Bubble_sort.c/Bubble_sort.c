#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define REPEAT 100  // repeat to get measurable time

// Bubble Sort function
void bubbleSort(int arr[], int n) {
    int i, j, temp;
    for(i = 0; i < n-1; i++) {
        for(j = 0; j < n-i-1; j++) {
            if(arr[j] > arr[j+1]) {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}

int main() {
    // array sizes to test
    int sizes[] = {1000, 2000, 3000, 4000, 5000, 6000, 7000,8000,9000,10000};
    int numSizes = sizeof(sizes) / sizeof(sizes[0]);

    srand(time(0));

    printf("  n\tTime (seconds)\n");
    printf("-------------------------\n");

    for(int s = 0; s < numSizes; s++) {
        int n = sizes[s];
        int arr[n], temp[n];

        // generate random numbers
        for(int i = 0; i < n; i++)
            arr[i] = rand() % 10000;

        clock_t start, end;
        double cpu_time;

        start = clock();
        for(int r = 0; r < REPEAT; r++) {
            // copy original array
            for(int i = 0; i < n; i++)
                temp[i] = arr[i];
            bubbleSort(temp, n);
        }
        end = clock();

        cpu_time = ((double)(end - start)) / CLOCKS_PER_SEC / REPEAT;

        printf("%5d\t%lf\n", n, cpu_time);
    }

    return 0;
}
