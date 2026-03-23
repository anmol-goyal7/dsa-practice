#include <iostream>
#include <string>

void reversestring (std::string arr[], int n) {
    int left{0}, right{n-1};

    while (left<right) {
        std::string temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;

        left++;
        right--;
    }
}

int main() {
    std::string arr[] = {"apple", "banana", "cherry", "date"};
    int n = 4;

    reversestring(arr, n);
 
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
 
    return 0;
}
