class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}
        n,m = len(s1) ,len(s2)

        def dp(i,j): #dp[i][j] = #min ascii deletion sum to make s[i:] and s2[j:] equal
            if i ==n and j == m:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if i ==n:
                ans = sum(ord(c) for c in s2[j:])
            elif j ==m:
                ans = sum(ord(c) for c in s1[i:])
            elif s1[i] == s2[j]:
                ans = dp(i+1,j+1)
            else:
                delete_s1 = ord(s1[i]) + dp(i+1,j)
                delete_s2 = ord(s2[j]) + dp(i,j+1)
                ans = min(delete_s1,delete_s2)
            memo[(i,j)] = ans
            return ans
        
        return dp(0,0)


