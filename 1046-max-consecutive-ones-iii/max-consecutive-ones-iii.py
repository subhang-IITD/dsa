class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        j = 0
        n = len(nums)
        mp = {}
        max_len = 0

        while j<n:
            if nums[j] == 0:
                if 0 not in mp:
                    mp[0] = 0
                mp[0] +=1

            while 0 in mp and mp[0] >k:
                if nums[i] ==0:
                    mp[0] -=1
                    if mp[0] == 0:
                        del mp[0]
                i+=1
            
            max_len = max(max_len , j-i+1)
            j+=1
        return max_len