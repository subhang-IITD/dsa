class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i =0
        odd_count = 0
        count =0

        for j in range(n):
            if nums[j] %2 == 1:
                odd_count +=1
            
            while odd_count >k:
                if nums[i] %2 ==1 :
                    odd_count-=1
                i+=1
            
            if odd_count ==k:
                count +=1
                temp = i
                while temp < j and nums[temp] %2 == 0: #cuz removing even numbers wont hurt
                    count +=1
                    temp +=1
            
        return count