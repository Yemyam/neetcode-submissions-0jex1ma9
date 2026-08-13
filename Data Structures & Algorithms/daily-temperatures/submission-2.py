class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        out = [0] * len(temperatures)
        # monotonic stack
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                popped = stack.pop()
                days = i - popped[1]
                out[popped[1]] = days
            
            stack.append((temp, i))
        return out

