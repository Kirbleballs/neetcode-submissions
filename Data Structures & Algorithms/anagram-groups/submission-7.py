class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def counter(string: str) -> dict:
            hash = dict()
            for char in string:
                if char in hash:
                    hash[char] += 1
                else:
                    hash[char] = 1
            return(hash)
        
        sublists_dict = dict()

        sublists = [] 

        for string in strs:
            i = 0
            if not sublists:
                sublists.append([string])
            else:
                while i < len(sublists) and counter(string) != counter(sublists[i][0]):
                    i+=1
                if i == len(sublists):
                    sublists.append([string])
                else:
                    sublists[i].append(string)
        
        return(sublists)

        
        
        
