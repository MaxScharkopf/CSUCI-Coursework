/*
 * Kevin Scrivnor
 * Copyright (C) 2025
 * COMP 362 - Operating Systems
 *
 * Modified by: Maxwell Scharkopf
 */

#include "matrixMult.h"

int
main(int argc, char** argv)
{
    // Input file should be passed to the program: ./matrixMult in.txt
    if (freopen(argv[1], "r", stdin) == 0) {
        oops("Cannot open the input file.\n", -1);
    }

    // two pairs of matrices
    int** a1,** b1,** c1;
    int** a2,** b2,** c2;

    // dimensions of the matices m x k and k x n
    int m1, k1, n1;
    int m2, k2, n2;

    allocateAndLoadMatrices(&a1, &b1, &c1, &m1, &k1, &n1);
    allocateAndLoadMatrices(&a2, &b2, &c2, &m2, &k2, &n2);

    // the real magic happens in there

    // Call multiply and join for the first pair of matrices
    pthread_t** tids1 = multiply(a1, b1, c1, m1, k1, n1);
    join(tids1, m1, n1);
    free_thread_ids(tids1, m1);

    // Call multiply and join for the second pair of matrices
    pthread_t** tids2 = multiply(a2, b2, c2, m2, k2, n2);
    join(tids2, m2, n2);
    free_thread_ids(tids2, m2);

    // dispaly results of matrix multiplication

    printf("\nMATRIX A1\n");
    displayMatrix(a1, m1, k1);
    freeMatrix(a1, m1);
    printf("\nMATRIX B1\n");
    displayMatrix(b1, k1, n1);
    freeMatrix(b1, k1);
    printf("\nMATRIX A1 x B1\n");
    displayMatrix(c1, m1, n1);
    freeMatrix(c1, m1);

    printf("\nMATRIX A2\n");
    displayMatrix(a2, m2, k2);
    freeMatrix(a2, m2);
    printf("\nMATRIX B2\n");
    displayMatrix(b2, k2, n2);
    freeMatrix(b2, k2);
    printf("\nMATRIX A2 x B2\n");
    displayMatrix(c2, m2, n2);
    freeMatrix(c2, m2);

    return 0;
}

// allocate space for the matricies the call @loadMatrix
// read m,k,n
// allocate (a,b,c) for the right size load (a,b) c is not made yet
void
allocateAndLoadMatrices(int*** a, int*** b, int*** c, int* m, int* k, int* n) {
    if (scanf("%d %d %d", m, k, n) == 0) {
        oops("Cannot read matrix sizes.\n", -2);
    }

    *a = malloc(sizeof(int*) * *m); // allocate row size for Matrix A
    for(int i = 0; i < *m; i++) (*a)[i] = malloc(sizeof(int) * *k); // allocate col size Matrix A
    loadMatrix(a, *m, *k);
    
    *b = malloc(sizeof(int*) * *k); // allocate row size for Matrix B
    for(int i = 0; i < *k; i++) (*b)[i] = malloc(sizeof(int) * *n); // allocate col size Matrix B
    loadMatrix(b, *k, *n);
    *c = malloc(sizeof(int*) * *m); // allocate row size for matrix B
    for(int i = 0; i < *m; i++) (*c)[i] = malloc(sizeof(int) * *n);// allocate col size Matrix C
}

// load the data (where?)
void
loadMatrix(int*** matrix, int m, int n)
{
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            scanf("%d", &((*matrix)[i][j]));
        }
    }
    displayMatrix(*matrix, m, n);
}

// print the matrix nicely (like activity)
void
displayMatrix(int** matrix, int m, int n)
{
    // TODO: implement
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            printf("%3d", (matrix)[i][j]);
        }
        printf("\n");
    }
}

// allocate thread id's
pthread_t**
alloc_tids(int m, int n)
{
    pthread_t **tids;

    tids = malloc(sizeof(pthread_t*) * m); // allocate row size for p_thread
    for(int i = 0; i < m; i++) (tids)[i] = malloc(sizeof(pthread_t) * n); // allocate col size
    
    return tids;
}

// create all the threads
pthread_t**
multiply(int** a, int** b, int** c, int m, int k, int n)
{
    pthread_t** thread_ids = alloc_tids(m, n);
    
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            MATRIX_CELL* cell = malloc(sizeof(MATRIX_CELL)); // Array of type MATRIX_CELL
            // Populate struct values
            cell->a = a;
            cell->b = b;
            cell->c = c;
            cell->i = i;
            cell->j = j;
            cell->k = k;
            
            pthread_create(&thread_ids[i][j], NULL, matrixThread, (void*)cell);
        }
    }
   
    return thread_ids;
}

// matrix thread does the calculation for a single cell ( like runner program)
void*
matrixThread(void* param)
{
    // map the parameter onto the structure
    MATRIX_CELL *cell = (MATRIX_CELL *)param;
    int **a = cell->a;
    int **b = cell->b;
    int **c = cell->c;
    int i = cell->i;
    int j = cell->j;
    int k = cell->k;
    
    // initialize to 0
    c[i][j] = 0;
    
    // perform dot product
    for(int x = 0; x < k; x++) {
        c[i][j] += a[i][x] * b[x][j];
    }

    free(cell);

    return NULL;
}

// wait for the threads (eventually... ) call after all the runner threads
void
join(pthread_t** tids, int m, int n)
{
    // Wait for all threads to complete
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            // Join each thread, passing NULL as we're not interested in the return value
            pthread_join(tids[i][j], NULL);
        }
    }
}

void
free_thread_ids(pthread_t** tids, int m)
{
    // Free each row of thread IDs
    for(int i = 0; i < m; i++) {
        free(tids[i]);
    }

    // Free the array of row pointers
    free(tids);
}

void
freeMatrix(int** matrix, int m)
{
    // Free each row of the matrix
    for(int i = 0; i < m; i++) {
        free(matrix[i]);
    }

    // Free the array of row pointers
    free(matrix);
}
