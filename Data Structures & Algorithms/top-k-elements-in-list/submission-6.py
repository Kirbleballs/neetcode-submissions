class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def counter(nums: list[int]) -> dict:
            hash = dict()
            for num in nums:
                if num in hash:
                    hash[num] += 1
                else:
                    hash[num] = 1
            return(list(hash.items()))

        def mergesort(arr) -> list:
            if len(arr) < 2:
                return(arr)

            mid = len(arr)//2
            left = arr[:mid]
            right = arr[mid:]

            leftsort = mergesort(left)
            rightsort = mergesort(right)
            return(merge(leftsort,rightsort))
        
        def merge(arr1,arr2) -> list:
            i,j = 0,0
            sort = []

            while i<len(arr1) and j<len(arr2):
                if arr1[i][1] < arr2[j][1]:
                    sort.append(arr1[i])
                    i += 1
                else:
                    sort.append(arr2[j])
                    j += 1
            
            sort.extend(arr1[i:])
            sort.extend(arr2[j:])
            return(sort)

        

        
        print(mergesort(counter(nums)))
        return([mergesort(counter(nums))[-i-1][0] for i in range(k)])



