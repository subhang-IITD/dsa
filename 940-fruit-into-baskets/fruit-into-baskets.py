class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i=0
        j=0
        n = len(fruits)
        mp = {}
        count =0
        max_len = 0

        while j<n:
            if fruits[j] not in mp or mp[fruits[j]] == 0:
                mp[fruits[j]] = 1
                count +=1
            else:
                mp[fruits[j]] += 1
            
            while count >2:
                mp[fruits[i]] -=1
                if mp[fruits[i]] == 0:
                    count -=1
                i+=1
            max_len = max(max_len,j-i+1)
            j+=1
        return max_len


