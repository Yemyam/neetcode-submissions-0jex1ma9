class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def climb(n):
            if n <= 1:
                return 1
            if n in cache:
                return cache[n]
            cache[n] = climb(n - 1) + climb(n - 2)
            return cache[n]
        return climb(n)