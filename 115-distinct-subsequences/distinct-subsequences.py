class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dp(i,j): #dp(i, j) → number of ways s[i:] can match t[j:] as a subsequence.
            if j == len(t):
                return 1
            if i==len(s):
                return 0 # j did not reach the end -> we did not create t using s
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i] == t[j]:
                ans = dp(i+1,j+1) + dp(i+1,j)
            else:
                ans = dp(i+1,j)
            memo[(i,j)] = ans
            return ans
        return dp(0,0)

# At every dp(i, j):
# 	•	If s[i] == t[j], we have two choices:
# 	1.	Use this match → dp(i+1, j+1)
# 	2.	Skip this character in s → dp(i+1, j)
# 	•	Add both results
# 	•	If s[i] != t[j] → only one choice:
# 	•	Skip s[i] → dp(i+1, j)


