#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define REPEAT 100  // repeat to get measurable average time

// Quick Sort partition function
int partition(int arr[], int low, int high) {
    int pivot = arr[high]; // choosing last element as pivot
    int i = low - 1;
    int temp;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            // swap arr[i] and arr[j]
            temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    // swap arr[i+1] and arr[high] (pivot)
    temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1;
}

// Quick Sort recursive function
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        // Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main() {
    // array sizes to test
    int sizes[] = {1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000};
    int numSizes = sizeof(sizes) / sizeof(sizes[0]);

    srand(time(0));

    printf("   n\tTime (seconds)\n");
    printf("---------------------------\n");

    for (int s = 0; s < numSizes; s++) {
        int n = sizes[s];
        int arr[n], temp[n];

        // generate random numbers
        for (int i = 0; i < n; i++)
            arr[i] = rand() % 10000;

        clock_t start, end;
        double cpu_time;

        start = clock();
        for (int r = 0; r < REPEAT; r++) {
            // copy original array
            for (int i = 0; i < n; i++)
                temp[i] = arr[i];
            quickSort(temp, 0, n - 1);
        }
        end = clock();

        cpu_time = ((double)(end - start)) / CLOCKS_PER_SEC / REPEAT;

        printf("%5d\t%lf\n", n, cpu_time);
    }

    return 0;
}
