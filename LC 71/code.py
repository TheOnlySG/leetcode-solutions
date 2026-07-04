class Solution:
    def simplifyPath(self, path: str) -> str:
        '''
        approch is simple , what ill do is split the given path from /'s
        present in the path. thus now we have a list of words in path.

        if the word is an empty string or a '.' , we will just continue to
        next iteration (which is exactly what the problem asks for)

        if it contains going to root using '..' , we will pop from the
        stack if it has anything in it.

        and if theres anything other than those things in the words , we
        will simply push it to stack.

        at last , we return the stack as a string by joining it with a /
        and also adding a / at start.

        TIme complexity : O(n)
        space complexity : O(n) , the stack + splits
        '''
        stack = []
        directories = path.split('/')
        for s in directories :
            if s == '' or s == '.':
                continue
            elif s == '..':
                if stack :
                    stack.pop()
            else :
                stack.append(s) 
        
        return '/' + '/'.join(stack)