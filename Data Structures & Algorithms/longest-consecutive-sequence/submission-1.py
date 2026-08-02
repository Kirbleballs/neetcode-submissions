class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxcount = 0
        for num in numset:
            current = num
            counter = 0
            if num - 1 not in numset:
                while current in numset:
                    current += 1
                    counter += 1
            maxcount = max(counter,maxcount)
        
        return(maxcount)
            
        