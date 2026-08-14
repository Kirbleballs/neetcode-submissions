class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        cut = (m+n) // 2

        if m > n:
            return(self.findMedianSortedArrays(nums2, nums1))
        
        lower = 0
        upper = m + 1
        mid = (lower + upper) // 2
        mid2 = cut - mid
        flag = True

        print(1)

        while flag == True:
            l1 = float('-inf') if mid == 0 else nums1[mid-1]
            r1 = float('inf') if mid == m else nums1[mid]
            l2 = float('-inf') if mid2 == 0 else nums2[mid2 - 1]
            r2 = float('inf') if mid2 == n else nums2[mid2]

            if l1 > r2:
                upper = mid
                mid = (lower + upper) // 2
                mid2 = cut - mid
            elif l2 > r1:
                lower = mid
                mid = (lower + upper) // 2
                mid2 = cut - mid
            else:
                flag = False
        
        print(l1, r1, l2, r2)
        if (m + n) % 2 == 0:
            return((max(l1,l2) + min(r1,r2)) / 2)
        else:
            return(min(r1,r2))



