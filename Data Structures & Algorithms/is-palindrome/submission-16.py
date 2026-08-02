class Solution:
    def isPalindrome(self, s: str) -> bool:
        ls =''
        for char in s:
            if (ord(char) > 64 and ord(char) < 91):
                ls += chr(ord(char) + 32)
                
            if (ord(char) > 96 and ord(char) < 123) or char in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
                ls += char
        print(ls)
        i = 0
        j = len(ls) - 1

        while i<j:
            if ls[i] != ls[j]:
                return(False)
            i+=1
            j-=1
            
        return(True)
        