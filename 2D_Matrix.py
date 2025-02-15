# Time complexity : O(log n)
# Space Complexity : O(1)
# Leetcode : Solved and submitted

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Finding the lenght of the matrix
        # If matrix row are 0, then return False as no element is present, then find the length of the columns
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        
        # put low as the first index and high as the last index
        low = 0
        high = m*n - 1
        
        # starting a while loop in a binary search
        while low <= high:
          
          # find the middle index
            mid = low + (high - low) // 2
            
            # extract the element at the middle index using the row = mid // 2 and column = mid % n
            mid_element = matrix[mid // n][mid % n]
            
            # Here we check for the target with the elements mid, low and high and act accordingly where to keep the search space, left side or right side
            # array
            if target == mid_element:
                return True
            elif target < mid_element:
                high = mid - 1
            else:
                low = mid + 1
        
        return False
                
