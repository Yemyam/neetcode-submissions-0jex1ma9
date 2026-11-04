class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # finding k
        # hours to finish a pile of bananas is ceil(pile_size / k)
        # only one pile can be finished per hour, so if len(piles) > h, then there exists no integer k
        # brute force solution:
        # iterate through all possible values of k, until the time to eat bananas exceeds h hours, then we return the previous k value
        # time complexity: O(n^2)
        # key insight: we can do a binary search on k, since we know the range of possible values is 1 - max(piles)
        # optimal time complexity: O(nlogn)

        l, r = 1, max(piles)
        min_hours = float("inf")
        out = 0
        while l < r:
            k = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                r = k
            else:
                l = k + 1
        return r
