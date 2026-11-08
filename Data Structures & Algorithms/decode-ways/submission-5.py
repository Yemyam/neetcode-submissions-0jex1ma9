class Solution:
    def numDecodings(self, s: str) -> int:
        # go through the string s, and recursively try and construct every possible combination of numbers
        # can we add memoization here?
        self.out = 0
        memo = {}
        def count(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            res = count(i + 1)
            if i < len(s) - 1:
                num = int(s[i] + s[i + 1])
                if num <= 26:
                    res += count(i + 2)
            memo[i] = res
            return res
        return count(0)
            
