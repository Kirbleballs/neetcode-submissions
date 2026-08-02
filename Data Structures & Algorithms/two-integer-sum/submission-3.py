class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        i = 0
        while nums[i] not in hash:
            hash[target - nums[i]] = i
            i += 1
        return([hash[nums[i]], i])