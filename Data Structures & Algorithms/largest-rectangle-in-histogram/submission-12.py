class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = []

        for i in range(len(heights)):
            if not stack:
                stack.append((heights[i],i))
            else:
                if heights[i] > stack[-1][0]:
                    stack.append((heights[i],i))
                else:
                    while stack and stack[-1][0] >= heights[i]:
                        idx = stack[-1][1]
                        maxarea = max((i - idx) * stack[-1][0], maxarea)  
                        stack = stack[:-1]
                        
                    stack.append((heights[i],idx))
        
        for height in stack:
            maxarea = max((len(heights) - height[1]) * height[0] , maxarea)

        return(maxarea)




