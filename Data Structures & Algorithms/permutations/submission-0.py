class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        possible = set(nums)
        curr = []
        out = []
        def backtrack(i, curr, possible):
            if i == len(nums):
                out.append(curr.copy())
                return
            for num in possible.copy():
                curr.append(num)
                possible.remove(num)
                backtrack(i + 1, curr, possible)
                curr.pop()
                possible.add(num)
        
        backtrack(0, curr, possible)
        return out
                
