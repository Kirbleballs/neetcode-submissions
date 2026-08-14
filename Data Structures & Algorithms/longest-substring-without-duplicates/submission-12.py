class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return(len(s))
        
        maxl = 1
        i = 0
        j = 1
        sset = {s[i]}

        while j < len(s):
            if s[j] not in sset:
                
                if maxl < j - i + 1:
                    maxl = j - i + 1
                
                sset.add(s[j])
                j += 1
            else:
                while s[j] in sset:
                    sset.remove(s[i])
                    i += 1

            
        return(maxl)
            


