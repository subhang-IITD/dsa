class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        
        reversed_s = s[::-1]
        n , m = len(s) , len(reversed_s)

        dp = [[0]*(m+1) for _ in range(n+1)]

        for i in range(n+1):
            for j in range(m+1):
                if i ==0 or j==0:
                    dp[i][j] = 0
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if s[i-1] == reversed_s[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        return dp[n][m]
