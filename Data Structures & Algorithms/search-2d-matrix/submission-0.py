class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])


        def pos(idx: int) -> tuple:
            r = idx // n
            c = idx % n
            return(r,c)
        
        lower = 0
        upper = m*n-1
        mid = (lower + upper) // 2

        while lower != mid:
            row = pos(mid)[0]
            col = pos(mid)[1]
            if matrix[row][col] < target:
                lower = mid
                mid = (lower + upper) // 2
            elif matrix[row][col] > target:
                upper = mid
                mid = (lower + upper) // 2
            else:
                return(True)
        
        if matrix[pos(lower)[0]][pos(lower)[1]] == target:
            return(True)
        if matrix[pos(upper)[0]][pos(upper)[1]] == target:
            return(True)
        return(False)






