from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        mp = Counter(p)
        count = len(mp)
        k = len(p)
        i = 0
        ans = []

        for j in range(len(s)):
            #include s[j] in the window
            if s[j] in mp:
                mp[s[j]] -= 1
                if mp[s[j]] == 0:
                    count -=1
            
            if j-i+1 ==k:
                if count ==0:
                    ans.append(i)

                if s[i] in mp:
                    mp[s[i]] +=1
                    if mp[s[i]] == 1:
                        count +=1
                i+=1
        return ans
                
                