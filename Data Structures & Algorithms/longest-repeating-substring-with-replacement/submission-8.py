class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) < 2:
            return len(s)
        
        output = 1
        i = 0
        j = 0

        counter = {}

        while j < len(s):
            if s[j] in counter:
                counter[s[j]] += 1
            else:
                counter[s[j]] = 1
            
            max_freq = max(counter.values())
            
            if max_freq + k >= j - i + 1:
                output = max(output, j - i + 1)
                j += 1
            else:
                counter[s[i]] -= 1
                i += 1
                j += 1
        
        return output