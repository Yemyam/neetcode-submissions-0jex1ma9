class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dfs returns the min amount of coints in order to reach the total
        # and add memoization
        memo = {}
        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]
            if remaining == 0:
                return 0
            elif remaining < 0:
                return float("inf")
            best = float("inf")
            for coin in coins:
                best = min(dfs(remaining - coin) + 1, best)
            memo[remaining] = best
            return best
            
        out = dfs(amount)
        if out == float("inf"):
            return -1
        return out