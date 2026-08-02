class Solution:
    def trap(self, height: List[int]) -> int:
        lpeak = 0
        rpeak = 0
        sum = 0
        for i in range(len(height)):
            if height[i] > height[lpeak]:
                lpeak, rpeak = i, i
            elif height[i] == height[lpeak]:
                rpeak = i
            sum += height[i]
        
        print(lpeak, rpeak, height[lpeak])
        
        lheight = height[:lpeak]
        rheight = height[:rpeak:-1]
        print(lheight)
        print(rheight)

        if lheight:
            lsum = lheight[0]
            for i in range(1,len(lheight)):
                lheight[i] = max(lheight[i], lheight[i-1])
                lsum += lheight[i]
        else:
            lsum = 0
            
        if rheight:
            rsum = rheight[0]
            for j in range(1,len(rheight)):
                rheight[j] = max(rheight[j], rheight[j-1])
                rsum += rheight[j]
        else:
            rsum = 0

        msum = height[lpeak] * (rpeak-lpeak+1)

        print(lsum, msum, rsum, sum)

        return(lsum + msum + rsum - sum)


                
        