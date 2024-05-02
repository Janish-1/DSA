#include <bits/stdc++.h>
using namespace std;

// Sorting Function
void insertionSort(int arr[],int n) {
    // Calling three variables
    int i, key, j;
    // Array for Sorting
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i-1;
        while (arr[j]>key && j >= 0){
            arr[j+1] = arr[j];
            j = j -1;
        }
        arr[j+1] = key;
    }
}

// Dry Run
// 12 11 13 5 6
// Step-1 :  key = 11  j = 0 arr[j] = 12 arr[j+1] = arr[j] j = j - 1 arr[j+1] = key

// A utility function to print an array
// of size n
void printArray(int arr[], int n) {
    int i;
    for (i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;
}

// Driver code
int main() {
    int arr[] = { 12, 11, 13, 5, 6 };
    int N = sizeof(arr) / sizeof(arr[0]);

    insertionSort(arr, N);
    printArray(arr, N);

    return 0;
}