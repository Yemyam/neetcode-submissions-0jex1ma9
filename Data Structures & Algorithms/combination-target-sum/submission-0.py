class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # we can create a decision tree to model this question, where at every layer in the decision tree we choose to include a value, or to exclude it
        # the base cases are when the target == total, and we add that to the output, or if total > target, we terminate the recursion
        out = []

        def dfs(i, curr, total):
            # base cases
            if total == target:
                out.append(curr.copy())
                return
            if total > target or i >= len(nums):
                return
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            curr.pop()
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return out
            