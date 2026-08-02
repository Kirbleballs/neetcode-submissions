class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftproduct = 1
        rightproduct = 1

        arr1 = [1]
        arr2 = [1]
        for i in range(len(nums)-1):
            leftproduct *= nums[i]
            arr1.append(leftproduct)

            rightproduct *= nums[-i-1]
            arr2.append(rightproduct)
        
        output = []
        for i in range(len(nums)):
            output.append(arr1[i] * arr2[len(nums)-i-1])
        
        return(output)
            

