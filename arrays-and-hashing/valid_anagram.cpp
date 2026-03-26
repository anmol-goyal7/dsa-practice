#include <stdio.h>
#include <string>
#include <unordered_map>

bool isAnagram(string s1, string s2) {
    unordered_map<char, int> map1, map2;

    for ( char c: s1) {
        map1[c]++;
    }

    for ( char c: s2) {
        map2[c]++;
    }

    if ( map1 == map2) {
        return true;
    }

    return false;

}

int main() { // the main function is AI generated.
    cout << isAnagram("listen", "silent") << endl;  // Output: 1 (true)
    cout << isAnagram("hello", "world") << endl;    // Output: 0 (false)
    cout << isAnagram("ab", "ba") << endl;          // Output: 1 (true)
    
    return 0;
}
