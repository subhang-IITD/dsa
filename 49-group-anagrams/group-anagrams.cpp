class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>> mp;
        for(string s : strs){
            string sorted = s;
            sort(sorted.begin(),sorted.end());
            mp[sorted].push_back(s);
        }
        vector<vector<string>> result;

        for(auto& kv : mp){
            result.push_back(kv.second);
        }
        return result;
    }
};