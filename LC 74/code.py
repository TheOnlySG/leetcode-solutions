class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        the idea is simple , we will be using the simple binary search as it is,
        by considering it is just as a simple 1D array.
        left will hold the value for start of subarray where the search will be
        started , and end or left will probably have the end index of subarray
        where the searching is done.
        
        to get the index of mid , we are using a simple trick :
        row of mid = mid index / number of elements in row
        colm of mid = mid index / number of elements in row
        '''


        
        i = len(matrix)
        j = len(matrix[0])

        if not i : return False

        left , right = 0 , i*j-1

        while left <= right :
            mid = (left + right) // 2 #index of mid
            currentElement = matrix[mid//j][mid%j] #value at index mid

            if currentElement == target :
                return True
            elif currentElement  > target :
                right = mid - 1
            else :
                left = mid + 1
            
        return False