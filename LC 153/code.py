class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        alr so we have to fit binary search in this question as it mentions
        time complexity.
        what we will do is if the nums[mid] gets greater than the nums[right]
        then it ofcourse mean the array is rotated and the smaller element lies
        in between mid to right (this 2nd half.)
        if thats not the case , it means the minimum element is in the first 
        half of the rotated array.
        '''

        left ,right = 0 , len(nums)-1
        while left < right:
            mid = (left+right) // 2
            if nums[mid] > nums[right] : #meaning right half is sorted
                left = mid + 1
            else :
                right = mid
        
        return nums[left]