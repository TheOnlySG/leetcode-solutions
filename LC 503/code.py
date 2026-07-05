class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        #resultant is the result array , we are initializing it to -1 each element
        resultant = [-1] * len(nums)
        stack = [] #stack is going to hold indexes of the array elements

        for i in range(2*len(nums)) :
            current = nums[i%len(nums)] #since the loops is going to run 2 times due to 2*len(nums),
            #we need to take remeinder in order to iterate 2 times
            while stack and nums[stack[-1]] < current: #if current element is greater than the stacks top index
                index = stack.pop() # take the index from stack , current is the next greater element of stacks top indexed element
                resultant[index] = current #set the stacks top indexed element to current in resultant
            
            if i < len(nums) :
                stack.append(i) # push the elements to stack

        return resultant