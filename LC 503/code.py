class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        numbers = '1234567890'
        for ch in s :
            if ch != ']':
                stack.append(ch)
            else :
                num = ''
                pieces = []
                while stack[-1] != '[' and stack[-1] not in numbers:
                    pieces.append(stack.pop())

                if stack[-1] == '[' : stack.pop()
                pieces.reverse()
                string = ''.join(pieces)
                if stack :
                    while stack and  stack[-1] in numbers:
                        num = num + stack.pop()
                num = 1 if num == '' else int(num[::-1]) 
                stack.append(string*num)
        
        return ''.join(stack)
        
