from typing import List

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        memo = {}
        
        def dp(mask):
            if mask == (1 << n) - 1:
                return 0
            if mask in memo:
                return memo[mask]
            i = bin(mask).count('1')
            ans = float('inf')
            for j in range(n):
                if not (mask & (1 << j)):
                    ans = min(ans, (nums1[i] ^ nums2[j]) + dp(mask | (1 << j)))
            memo[mask] = ans
            return ans
        
        return dp(0)
