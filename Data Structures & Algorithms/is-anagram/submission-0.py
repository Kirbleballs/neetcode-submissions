class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def counter(string):
            hash = dict()
            for char in list(string):
                if char in list(hash):
                    hash[char] += 1
                else:
                    hash[char] = 1
            return(hash)
        
        if counter(s) == counter (t):
            return(True)
        else:
            return(False)
        



        