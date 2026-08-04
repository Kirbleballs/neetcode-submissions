class Solution:
    def findMin(self, nums: List[int]) -> int:
        lower = 0
        upper = len(nums) - 1
        mid = (lower + upper) // 2
        print(lower, upper, mid, nums[mid], nums[0])
        
        while lower != mid:
            if nums[mid] > nums[0]:
                lower = mid
                mid = (lower + upper) // 2
            elif nums[mid] < nums[0]:
                upper = mid
                mid = (lower + upper) // 2
            print(lower, upper, mid, nums[mid], nums[0])
        
        if lower == len(nums) - 2:
            if nums[upper] < nums[0]:
                return(nums[upper])
            else:
                return(nums[0])
        return(nums[upper])
        
        