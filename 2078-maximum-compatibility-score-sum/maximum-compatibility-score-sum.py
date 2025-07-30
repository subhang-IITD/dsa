class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        n = len(students[0])
        memo = {}

        def get_score(s,t): # student, teacher
            cnt = 0
            for i in range(n):
                if s[i] == t[i]:
                    cnt+=1
            return cnt
        
        def dp(mask,i):
            if i == m:
                return 0
            if (mask,i) in memo:
                return memo[(mask,i)]
            
            ans = 0
            for j in range(m):
                if (mask & (1<<j)) == 0:
                    score = get_score(students[i],mentors[j])
                    new_mask = mask | (1<<j)
                    ans = max(ans , score + dp(new_mask,i+1))
            
            memo[(mask,i)] = ans
            return ans
        return dp(0,0)
        