class Solution:

    def encode(self, strs: List[str]) -> str:
        code =str()
        for s in strs:
            code += str(len(s)) + '#' + s
        print(code)
        return(code)


    def decode(self, s: str) -> List[str]:
        i = 0
        list = []
        while i < len(s):
            length = 0
            while s[i] != '#':
                length *= 10
                length += int(s[i])
                i += 1
            list.append(s[i+1 : i+1+length])
            i = i+1+length
        return(list)
            
            

        
