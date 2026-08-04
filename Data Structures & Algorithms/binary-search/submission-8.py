class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower = 0
        upper = len(nums) - 1
        mid = (upper + lower)//2

        while mid != lower:
            if nums[mid] > target:
                upper = mid
            elif nums[mid] < target:
                lower = mid
            else:
                return(mid)
            
            mid = (upper + lower) // 2
        
        if nums[lower] == target:
            return(lower)
        elif nums[upper] == target:
            return(upper)
        else:
            return(-1)


          