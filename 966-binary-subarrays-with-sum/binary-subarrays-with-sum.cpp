class Solution {
public:
    int numSubarraysWithSum(vector<int>& nums, int goal) {
        int n = nums.size();
        int i = 0;
        int curr_sum = 0;
        int count = 0;

        for (int j = 0; j < n; j++) {
            curr_sum += nums[j];

            while (curr_sum > goal) {
                curr_sum -= nums[i];
                i++;
            }

            if (curr_sum == goal) {
                // count all windows ending at j from i
                int left = i;
                while (left <= j && curr_sum == goal) {
                    count++;
                    if (nums[left] == 1)
                        break;
                    left++;
                }
            }
        }
        return count;
    }
};
