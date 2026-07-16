class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left , right = 0 , len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            #there are 3 possibilities , 1st when nums[mid] is the target 
            #element
            if nums[mid] == target : return mid

            #possibility 2 : first half , or part before mid is sorted.
            elif nums[mid] >= nums[left] :
                #target is present
                #in between 1st half of the rotated list , 
                #which is in between range left to mid
                if nums[mid] >= target and target >= nums[left] :
                    right = mid - 1
                else : #present in the other half of list 
                    left = mid + 1
            else :
                if nums[mid] <= target and target <= nums[right] :
                    left = mid + 1
                else :
                    right = mid - 1
        return -1