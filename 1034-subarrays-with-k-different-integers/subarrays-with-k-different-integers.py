class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        def atmostK(nums,k):
            count = 0
            i=0
            mp = {}
            unique = 0
            for j in range(len(nums)):
                if nums[j] not in mp or mp[nums[j]] == 0:
                    mp[nums[j]] =1
                    unique +=1
                else:
                    mp[nums[j]] +=1
            

                while unique > k:
                    mp[nums[i]] -=1
                    if mp[nums[i]] == 0:
                        unique-=1
                    i+=1

                count += j-i+1
            return count
        return atmostK(nums,k) - atmostK(nums,k-1)