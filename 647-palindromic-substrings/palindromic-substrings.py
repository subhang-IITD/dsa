class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memo = {}
        count =0

        def dp(i,j):
            if i > j:
                return True
            if i == j:
                return True
            if s[i] != s[j]:
                return False
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = dp(i+1,j-1)
            return memo[(i,j)]
        
        for i in range(n):
            for j in range(i,n):
                if dp(i,j):
                    count +=1
        return count 
