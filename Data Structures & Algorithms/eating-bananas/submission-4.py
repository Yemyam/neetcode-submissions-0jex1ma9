import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # we know that k cannot be larger than max(piles)
        l = 1
        r = max(piles)
        while l < r:
            m = (l + r) // 2
            hours = sum(math.ceil(pile / m) for pile in piles)

            if hours <= h:
                r = m

            else:
                l = m + 1
        
        return l
