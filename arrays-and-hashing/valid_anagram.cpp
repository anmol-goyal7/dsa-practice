class Solution {
public:
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
};
