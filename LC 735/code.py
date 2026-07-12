class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        main intution behind the problem :
        astroids are freely flying into open space , and there direction is noted by their nature.
        positive = right , negetive = left.
        2 astroids will collide if they are into opposite directions.
        the collision will cause 1 of them or both of them to explode. the greater absolute sized 
        asteroid survives and the other explodes. if they have same absolute value then both explode.

        the problem can be solved using stack at O(n) time and space.
        '''

        stack = []

        for asteroid in asteroids :
            while stack and asteroid < 0 and stack[-1] > 0 :
                difference = stack[-1] - abs(asteroid) #find absulute difference between astroid and stack top
                if difference < 0 : 
                    stack.pop()
                elif difference > 0 :
                    asteroid = 0
                else :
                    asteroid = 0
                    stack.pop()

            if asteroid :
                stack.append(asteroid)
        return stack