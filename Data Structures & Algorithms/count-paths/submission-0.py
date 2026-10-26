class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # how many ways can we arrange m downs and n rights
        return int(math.factorial(n - 1 + m - 1) / (math.factorial(n - 1) * math.factorial(m - 1)))