class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        '''
        stack will store the expression
        idology :
        1. keep appending until +-*/
        2. pop 2 elements once an operator hits.
        3. perform operation according to operator
        4. push the answer into stack

        while doing / , truncate towards zero (fancy words) , means 
        just use the integral part of float answer. we can handle it by
        // in python but thats floor division and it behaves different
        in negetive numbers so we will stick with type casting
        '''

        stack = []

        for token in tokens : 
            if token in '+-/*':
                after = stack.pop()
                before = stack.pop()
                result = 0
                match token:
                    case '+':
                        result = after + before
                    case '-':
                        result = before - after
                    case '*' :
                        result = after * before
                    case '/':
                        result = int(before / after) 
                    case _ :
                        pass
                    
                stack.append(result)
                
            else :
                stack.append(int(token))
            
        return stack[-1]