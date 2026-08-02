class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        comb = [(target - position[i], (target-position[i]) / speed[i]) for i in range(len(position))]
        
        def msort(arr):
            if len(arr) < 2:
                return(arr)
            
            mid = len(arr)//2
            l = arr[:mid]
            r = arr[mid:]

            ls = msort(l)
            rs = msort(r)
            return(merge(ls, rs))

        def merge(arr1,arr2):
            i = 0
            j = 0
            sort = []

            while i<len(arr1) and j<len(arr2):
                if arr1[i][0] < arr2[j][0]:
                    sort.append(arr1[i])
                    i+=1
                else:
                    sort.append(arr2[j])
                    j+=1
            
            sort.extend(arr1[i:])
            sort.extend(arr2[j:])

            return(sort)
        
        

        stack = []

        for car in msort(comb):
            if not stack:
                stack.append(car[1])
            else:
                if car[1] > stack[-1]:
                    stack.append(car[1])
    
        


        return(len(stack))
        