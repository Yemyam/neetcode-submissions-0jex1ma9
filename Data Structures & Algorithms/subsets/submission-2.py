class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for every element in the array we can chose to include it, or exclude it from the current subset. 
        # We will make n binary decisions for an array of length n,
        # meaning that we will have 2 ^ n distinct subsets
        out = []
        curr = []
        def backtrack(i, curr):
            if i == len(nums):
                out.append(curr.copy())
                return
            curr.append(nums[i])
            backtrack(i + 1, curr)
            curr.pop()
            backtrack(i + 1, curr)
        
        backtrack(0, curr)
        return out
