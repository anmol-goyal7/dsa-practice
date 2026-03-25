#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> twoSum(vector<int>& arr, int target) {
    unordered_map <int, int> seen;

    for (int i = 0; i < arr.size(); i++) {
    
        int complement = target - arr[i];

        if (seen.count(complement)) {
            return {seen[complement], i};
        }

        seen[arr[i]] = i;
        }
    return {};
    
}

int main() {
    vector<int> arr = {2, 7, 11, 15};
    int target = 9;
        
    vector<int> result = twoSum(arr, target);
    cout << result[0] << " " << result[1];  
    
    return 0;
}
