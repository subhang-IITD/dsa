class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        mp = Counter(t)
        i=0
        j=0
        count = len(mp)
        min_length = float("inf")
        start = 0
        n = len(s)

        while j<n:

            if s[j] in mp:
                mp[s[j]] -=1
                if mp[s[j]] ==0:
                    count -=1

            while count ==0:
                if j-i+1 < min_length:
                    min_length = j-i+1
                    start = i
                
                if s[i] in mp:
                    mp[s[i]]+=1
                    if mp[s[i]] >0:
                        count +=1
                i+=1
            j+=1
        
        return "" if min_length == float("inf") else s[start : start + min_length]
