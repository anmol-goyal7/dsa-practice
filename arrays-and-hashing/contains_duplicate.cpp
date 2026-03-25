#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

bool containsDuplicate(vector<int>& nums) {

    unordered_set<int> seen;
    
    for (int i = 0; i < nums.size(); i++) {
   
        if (seen.count(nums[i])) {
            return true;
        }
        else {
            seen.insert(nums[i]);
        }
    }
    
    return false;
}

int main() {

    vector<int> nums1 = {1, 2, 3, 1};
    vector<int> nums2 = {1, 2, 3, 4};
    vector<int> nums3 = {99, 99};
    
    cout << containsDuplicate(nums1) << '\n';
    cout << containsDuplicate(nums2) << '\n';  
    cout << containsDuplicate(nums3) << '\n';  
    
    return 0;
}
