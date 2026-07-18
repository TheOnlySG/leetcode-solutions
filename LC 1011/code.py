class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left , right = max(weights) , sum(weights)
        resultant = right

        def works(capacity):
            requiredDays , currCapacity = 1 , capacity
            for w in weights :
                if currCapacity - w < 0 :
                    requiredDays += 1
                    currCapacity = capacity
                currCapacity -= w
            return requiredDays <= days

        while left <= right :
            capacity = (left + right) // 2
            if works(capacity):
                resultant = min(resultant , capacity)
                right = capacity - 1
            else :
                left = capacity + 1
        return resultant