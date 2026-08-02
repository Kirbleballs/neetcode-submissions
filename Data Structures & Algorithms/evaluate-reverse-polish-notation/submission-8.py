class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0 
        operators = {'+', '-', '*', '/'}
        stack = list()

        while i < len(tokens):
            print(stack, tokens[i])
            if tokens[i] not in operators:
                stack.append(int(tokens[i]))
            else:
                if tokens[i] == '+':
                    result = stack[-2] + stack[-1]
                elif tokens[i] == '-':
                    result = stack[-2] - stack[-1]
                elif tokens[i] == '*':
                    result = stack[-2] * stack[-1]
                else:
                    if stack[-2] * stack[-1] > 0:
                        result = stack[-2] // stack[-1]
                    else:
                        result = (-1) * (-stack[-2] // stack[-1])

                stack = stack[:-2]
                stack.append(result)
            i+=1
        return(stack[0])






