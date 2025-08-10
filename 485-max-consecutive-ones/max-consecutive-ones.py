class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0 
        n = len(nums)
        ans = 0

        for num in nums:
            if num == 1:
                counter +=1 
                ans = max(ans,counter)
            else:
                counter = 0
        return ans