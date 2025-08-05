#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int id;  // Job ID
    int x;   // Deadline
    int y;   // Profit
} Pair;

// Comparator function for sorting by profit in descending order
int compareProfit(const void *a, const void *b) {
    Pair *p1 = (Pair *)a;
    Pair *p2 = (Pair *)b;
    
    return p2->y - p1->y; // Descending order (highest profit first)
}

int main(int argc, const char *argv[]) {
    
    int deadline, profit;
    int jobs = 0;
    
    // Read the number of jobs
    scanf("%d", &jobs);

    // Allocate memory for jobs
    Pair *arr = malloc(sizeof(Pair) * jobs);
    
    if (arr == NULL) {
        printf("Memory allocation failed.\n");
        return 1; // Exit if malloc fails
    }

    // Read job details into the array
    int max_deadline = 0; // Track largest deadline
    for (int i = 0; i < jobs; i++) {
        scanf("%d %d", &deadline, &profit);
        arr[i].id = i + 1;  // Assign initial IDs before sorting
        arr[i].x = deadline;
        arr[i].y = profit;

        if (deadline > max_deadline) {
            max_deadline = deadline; // Update max deadline
        }
    }

    // Sort jobs based on profit (highest to lowest)
    qsort(arr, jobs, sizeof(Pair), compareProfit);

    // Assign new IDs from 1 to `jobs` after sorting
    for (int i = 0; i < jobs; i++) {
        arr[i].id = i + 1;  // Reassign sorted IDs
    }

    // Create an empty schedule array of size max_deadline
    int *schedule = malloc(sizeof(int) * max_deadline);
    if (schedule == NULL) {
        printf("Memory allocation for schedule failed.\n");
        free(arr);
        return 1;
    }

    // Initialize all slots to -1 (indicating empty)
    for (int i = 0; i < max_deadline; i++) {
        schedule[i] = -1;
    }

    int total_profit = 0; // Track total profit from scheduled jobs

    // Slot jobs into the schedule array
    for (int i = 0; i < jobs; i++) {
        int slot = arr[i].x - 1; // Adjust deadline to 0-based index

        // Traverse left to find an available slot
        while (slot >= 0 && schedule[slot] != -1) {
            slot--;
        }

        // If a free slot is found, place the job there
        if (slot >= 0) {
            schedule[slot] = arr[i].id; // Store job ID
            total_profit += arr[i].y;   // Add job's profit to total
        }
    }

    // Print results for verification
    printf("\nSorted Jobs (Highest Profit First):\n");
    for (int i = 0; i < jobs; i++) {
        printf("Job ID %d -> Deadline: %d, Profit: %d\n", arr[i].id, arr[i].x, arr[i].y);
    }

    printf("\nMax Deadline: %d\n", max_deadline);
    printf("Final Scheduled Jobs: ");
    for (int i = 0; i < max_deadline; i++) {
        if (schedule[i] == -1)
            printf("[Empty] ");
        else
            printf("[Job %d] ", schedule[i]);
    }
    printf("\n");

    // Print total profit
    printf("Total Profit: %d\n", total_profit);

    // Free allocated memory
    free(arr);
    free(schedule);

    return 0;
}
