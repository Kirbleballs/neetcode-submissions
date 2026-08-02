class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash = {')': '(', ']' : '[', '}':'{'}
        for char in s:
            if char in {'(' , '[', '{'}:
                stack.append(char)
            else:
                if not stack or stack[-1] != hash[char]:
                    return(False)
                else:
                    stack = stack[:-1]
        if stack:
            return(False)
        else:
            return(True)
                

        