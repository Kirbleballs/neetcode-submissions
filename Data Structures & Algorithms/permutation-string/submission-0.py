class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def counts(s:str) -> dict:
            counter = dict()
            for char in list(s):
                if char in counter:
                    counter[char] += 1
                else:
                    counter[char] = 1
            
            return(counter)
        
        check = counts(s1)
        
        for i in range(0,len(s2) - len(s1) + 1):
            if counts(s2[i:i+len(s1)]) == check:
                return(True)
        
        return(False)

