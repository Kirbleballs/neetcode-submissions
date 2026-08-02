class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def msort(arr):
            if len(arr) < 2:
                return(arr)
            
            mid = len(arr)//2
            l = arr[:mid]
            r = arr[mid:]

            lsort = msort(l)
            rsort = msort(r)
            return(merge(lsort,rsort))

        def merge(arr1,arr2):
            i = 0
            j = 0
            sort =[]

            while i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    sort.append(arr1[i])
                    i += 1
                else:
                    sort.append(arr2[j])
                    j += 1
            
            sort.extend(arr1[i:])
            sort.extend(arr2[j:])

            return(sort)
        
        ms_nums = msort(nums)
        sols = set()

        for i in range(len(ms_nums)-2):
            j = i+1
            k = len(ms_nums) - 1

            while j != k:
                if ms_nums[i] + ms_nums[j] + ms_nums[k] == 0:
                    sols.add((ms_nums[i],ms_nums[j],ms_nums[k]))
                    j += 1
                elif ms_nums[i] + ms_nums[j] + ms_nums[k] < 0:
                    j += 1
                else:
                    k -= 1
        
        return(list(sols))

                

                







