class Solution:
    def removeDuplicates(self, s: str) -> str:
        '''
        approch :
        we will use stack , push each element in stack as the loop iterates. if
        element which we are iterating on s , appers on top of stack , then we
        know its adjecent. so we wil just pop from stack and move ahead.
        complexity : time O(n) , space O(1)

        '''
        stack = []
        for ch in s :
            if not stack :
                stack.append(ch)
            elif stack[-1] == ch :
                stack.pop()
            else :
                stack.append(ch)
        return ''.join(stack)