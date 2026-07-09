class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        This is simple and straight forward a stack question. we are going
        to build a monotonus stack. the algo follows following flow :
        1. iterate for each charecter in given string 'num'
        2. if charecter is smaller than the stack's top , we will keep
        popping. (while maintaining the k counter)
        3. once the loop ends , we have a stack in increasing order , and
        if k is still left , we can just remove elements from end of the stack
        to make the returning string as small as possible.
        4. now , some times , edge cases include our answer to be '' , an 
        empty string. we will straight away handle it by returning '0' , if
        the string is empty.

        time complexity : O(n)
        space complexity : O(1),
        where n is len(num)
        '''
        
        stack = []
        for ch in num :
            while stack and k and int(stack[-1]) > int(ch) :
                stack.pop()
                k -= 1

            stack.append(ch)

        while k:
            stack.pop()
            k -= 1
        answer = (''.join(stack)).lstrip('0')
        if answer == '' : return '0'
        return answer
        