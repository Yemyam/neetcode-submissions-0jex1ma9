class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for every element we can choose to keep it or omit it
        out = []

        curr = []
        def dfs(i):
            if i == len(nums):
                out.append(curr.copy())
                return
            # include the ith element
            curr.append(nums[i])
            dfs(i + 1)

            # omit the ith element
            curr.pop()
            dfs(i + 1)
        
        dfs(0)
        return out