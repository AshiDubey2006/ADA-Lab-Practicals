#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int n, i, j, last_finish;

    srand(time(0));
    n = rand() % 10 + 1; // random number between 1 and 10
    int start[n], finish[n];

    // Generate random start & finish times
    for (i = 0; i < n; i++) {
        start[i] = rand() % 10;           // 0–9
        finish[i] = start[i] + (rand() % 6 + 1); // start+1 to start+6
    }

    // Print generated activities
    printf("Number of activities: %d\n", n);
    printf("Generated activities:\n");
    for (i = 0; i < n; i++)
        printf("A%d: start=%d, finish=%d\n", i + 1, start[i], finish[i]);

    // Sort activities by finish time (simple bubble sort)
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (finish[j] > finish[j + 1]) {
                int temp = finish[j];
                finish[j] = finish[j + 1];
                finish[j + 1] = temp;

                temp = start[j];
                start[j] = start[j + 1];
                start[j + 1] = temp;
            }
        }
    }

    // Select activities using Greedy method
    printf("\nSelected activities:\n");
    printf("A1: start=%d, finish=%d\n", start[0], finish[0]);
    last_finish = finish[0];

    for (i = 1; i < n; i++) {
        if (start[i] >= last_finish) {
            printf("A%d: start=%d, finish=%d\n", i + 1, start[i], finish[i]);
            last_finish = finish[i];
        }
    }

    return 0;
}
