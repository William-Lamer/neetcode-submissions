class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        width = len(matrix[0])
        height = len(matrix)

        l = 0
        r = (width * height) - 1

        while l <= r: 
            mid = (l + r) // 2
            height_pos = mid // width
            width_pos = mid % width
            value = matrix[height_pos][width_pos]
           
            if value == target: 
                return True
            
            if target < value:
                r = mid - 1
            elif target > value: 
                l = mid + 1

        
        return False