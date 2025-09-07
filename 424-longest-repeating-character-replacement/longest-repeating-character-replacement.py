class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        i = 0
        n = len(s)
        max_len = 0

        for j in range(len(s)):
            if s[j] not in mp:
                mp[s[j]] = 1
            else:
                mp[s[j]] +=1
            
            window_size = j-i+1
            max_count = max(mp.values())

            
            while window_size - max_count  > k:
                mp[s[i]] -=1
                i+=1
                window_size = j-i+1
                max_count = max(mp.values())
            
            max_len = max(max_len , window_size)
        return max_len