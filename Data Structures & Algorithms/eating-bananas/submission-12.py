class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        most = float('-inf')
        for bananas in piles:
            most = max(most,bananas)
        
        lower = 1
        upper = most
        mid = (lower + upper) // 2

        hours = 0
        for bananas in piles:
            hours += (bananas + mid - 1) // mid
            

        print(lower, upper, mid, hours)

        while lower != mid:
            
            
            hours = 0
            for bananas in piles:
                hours += -1 * (-bananas // mid)
                print(hours)
            if hours > h:
                lower = mid
                mid = (lower + upper) // 2
            elif hours <= h:
                upper = mid
                mid = (lower + upper) // 2
                
            
            print(lower, upper, mid, hours)
        hours = 0
        
        for bananas in piles:
            hours += -1 * (-bananas // mid)
        if hours <= h:
            return(mid)
        else:
            return(upper)            
        
             




                
        