class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = list()
        output = [0 for i in range(len(temperatures))]

        for i in range(len(temperatures)):
            if stack:
                while stack and stack[-1][0] < temperatures[i]:
                    output[stack[-1][1]] = i - stack[-1][1]
                    stack = stack[:-1]
            stack.append((temperatures[i],i))
        
        return(output)
            

        