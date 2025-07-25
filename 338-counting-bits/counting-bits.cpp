class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> result;
        for(int i=0;i<=n;i++){
            result.push_back(counter(i));
        }
        return result;
    }

    int counter(int num){
        int count = 0;
        while(num>0){
            num &=num&(num-1);
            count++;
        }
        return count;
    }
};