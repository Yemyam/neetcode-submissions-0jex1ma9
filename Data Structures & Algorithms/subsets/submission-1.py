class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for every element we can choose to keep it or omit it
        out = []
        curr = []
        def backtrack(i):
            if i == len(nums):
                out.append(curr.copy())
                return
            curr.append(nums[i])
            backtrack(i + 1)
            curr.pop()
            backtrack(i + 1)
        backtrack(0)
        return out